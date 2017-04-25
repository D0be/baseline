#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import re
import time
import random
import lib.log as log
import lib.backup as backup


class Pass(object):
	"""Profile repair(HISTSIZE/TMOUT)"""

	def __init__(self,data,isrepair):
		self.data = data
		self.isrepair= isrepair
		self.target_filename = "./target_file/profile"
		self.msg = ''

	def verfiy(self,term):#判断怎样修复，返回修复等级
		with open(self.target_filename,"r") as f:
			data= f.read()	#读取目标文件内容
			#print data

		for n in term:						# i 传过来的数组内容  遍历 n（i 的key）
			if n !=	'update':			# 如果 n 不为 update   
				str = n

		patt = r'(%s)=(\d{1,4})' % str	#正则
		# print patt
		m = re.search(patt,data)	# 匹配文件中的所要修改的内容
		# print m.group(2)	#得到目标文件的值
		# print term[str]	#正确值
		
		if m:							# 如果匹配成功
			if int(m.group(2)) == int(term[str]):	#判断安全的标准  每个文件的都不一样
				r=0
			else:
				r=1
		else:
			r=2
		self.msg = self.target_filename+'=> project: '+str
		log.print_check_log(self.msg,r)
		return r
		
	def repair(self,term,level):
		if  level==1:	# r==1  存在不安全  需要编辑配置文件
			self.edit_config(term)
		elif level==2:	# r==2   没有配置选项   需要增加一个
			self.add_config(term)
		elif level==0:	# r==0   安全 无须 修复
			log.print_check_log(self.msg+' Don\'t need repair .Because it' ,0)
		else:	# 其他值 则报错
			log.print_check_log('Error',2)

	def edit_config(self,term):
		self.backup()
		print "更新配置中..."

		for n in term:						# i 传过来的数组内容  遍历 n（i 的key）
			if n !=	'update':			# 如果 n 不为 update   
				str = n

		newconfig = str+'='+term['update']
		print newconfig	#正确值

		patt = r'(%s)=(\d{1,4})' % str		#正则
		#print patt
		with open(self.target_filename,"r") as f:
			data= f.read()	#读取目标文件内容
		data = re.sub(patt, newconfig, data)
		with open(self.target_filename,"w") as f:
			f.write(data)	#读取目标文件内容

		print "更新成功!"

	def add_config(self,term):
		self.backup()
		for n in term:						# i 传过来的数组内容  遍历 n（i 的key）
			if n !=	'update':			# 如果 n 不为 update   
				str = n

		newconfig = str+'='+term['update'] + "\n"
		print newconfig	#正确值

		with open(self.target_filename,"a+") as f:
			f.write(newconfig + "\n")

		log.print_repaire_log(self.msg)

	def backup(self):
		with open(self.target_filename,"r") as f:
			data= f.read()	#读取目标文件内容
		filename = self.target_filename.split('/')[-1]
		backup_name = filename + str(int(time.time())) + str(random.randint(100,999)) + '.bak'
		#print backup_name
		with open(backup_name,"w") as f:
			f.write(data)	#读取目标文件内容
		log.print_repaire_log(self.msg)

	def echo_data(self):
		print self.data

	def run(self):
		#self.echo_data()
		backup.moveFileto(self.target_filename)
		for term in self.data:	#遍历每个修改项
			level = self.verfiy(term)	#返回需要修复的等级，如更新、添加、无需修复
			#print level
			if self.isrepair==True:
				self.repair(term,level)


if __name__=='__main__':
	data = [{'update': '100', 'HISTSIZE': '100'}, 
			{'update': '180', 'TMOUT': '180'}]
	isrepair=False
	Pass=Pass(data,isrepair)
	Pass.run()

