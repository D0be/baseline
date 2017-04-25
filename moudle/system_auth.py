#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
import lib.log as log
import lib.backup as backup 
import re
import time
import random


class Pass(object):
	"""alias repair"""
	def __init__(self,data,isrepair):
		self.data = data
		self.isrepair = isrepair
		self.target_filename = "./target_file/system-auth"
		self.msg = ''

	def verfiy(self,term):#判断怎样修复，返回修复等级
		r = 0
		with open(self.target_filename,"r") as f:
			data= f.read()	#读取目标文件内容
			#print data

		for n in term:						# i 传过来的数组内容  遍历 n（i 的key）
			if n !=	'update':			# 如果 n 不为 update   
				str = n

		patt = r"pam_cracklib\.so\s+minlen=\d+\s+ucredit=-\d+\s+lcredit=-\d+\s+dcredit=-\d+\s+ocredit=-\d+"		#正则
		# print patt
		m = re.search(patt,data)   		# 匹配文件中的所要修改的内容
		# print m.group(1)			#得到目标文件的值
		# print term[str]	#正确值
		# print m
		if m:							# 如果匹配成功
			pass
		else:
			r = 2
		self.msg = self.target_filename+'=> project: '+str
		log.print_check_log(self.msg,r)
		return r
	def repair(self,term,level):
		#print "fliname :alias"
		if  level==1:	# r==1  存在不安全  需要编辑配置文件
			self.edit_config(term)
		elif level==2:	# r==2   没有配置选项   需要增加一个
			self.add_config(term)
		elif level==0:	# r==0   安全 无须 修复
			log.print_check_log(self.msg+' Don\'t need repair .Because it' ,0)
		else:	# 其他值 则报错
			log.print_check_log(self.msg,2)

	def edit_config(self,term):
		pass

	def add_config(self,term):
		for n in term:						# i 传过来的数组内容  遍历 n（i 的key）
			if n !=	'update':			# 如果 n 不为 update   
				str = n
		newconfig = 'pam_cracklib.so minlen=6 ucredit=-1   lcredit=-1   dcredit=-1'
		print newconfig	#正确值

		with open(self.target_filename,'r+') as f:
			data = f.read()
			data = re.sub(r'pam_cracklib.so',newconfig,data)
		with open(self.target_filename,'w+') as f:
			f.write(data)
		log.print_repaire_log(self.msg)



	def echo_data(self):
		print self.data

	def run(self):
		backup.moveFileto(self.target_filename)	
		#self.echo_data()
		#backup.moveFileto(self.target_filename)
		for term in self.data:	#遍历每个修改项
			#print term.keys()[0]    //返回PASS_MAX_DAYS
			level = self.verfiy(term)	#返回需要修复的等级，如更新、添加、无需修复
			#print level
			if self.isrepair == True:
				self.repair(term,level)


if __name__=='__main__':
	data = [{'update':'','passdiffcult':''}]
	isrepair=True
	Pass=Pass(data,isrepair)
	Pass.run()