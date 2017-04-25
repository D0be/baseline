#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import sys
import re
import time
import random
import lib.log as log
import lib.backup as backup


class Pass(object):
	"""password repair"""

	def __init__(self,data,isrepair):
		self.data = data
		self.isrepair= isrepair
		self.target_filename = ""
		self.msg = ''

	def verfiy(self,term):#判断怎样修复，返回修复等级
		target_filename = term.keys()[0]
		with open(target_filename,"r") as f:
			data= f.read()	#读取目标文件内容
			#print data
		#print target_filename
		for n in term:
			if n != 'update':
				str =n 
		patt = "\numask.*?(\d{3})"	#正则
		# print patt
		m = re.search(patt,data)   		# 匹配文件中的所要修改的内容
		#print m.group(1),m.group(3)				#得到目标文件的值
		#print term[str]	#正确值
		
		if m:							# 如果匹配成功
			if m.group(1) == '027':	#判断安全的标准  每个文件的都不一样
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
		self.backup(term)
		target_filename = term.keys()[0]
		newconfig = 'umask ' + term[target_filename]
		print newconfig	#正确值

		patt = "\numask.*?(\d{3})"		#正则
		#print patt
		with open(target_filename,"r") as f:
			data= f.read()	#读取目标文件内容
		data = re.sub(patt, newconfig, data)
		with open(target_filename,"w") as f:
			f.write(data)	#读取目标文件内容
		log.print_repaire_log(self.msg)

	def add_config(self,term):
		for n in term:
			if n !=	'update':
				target_filename = n

		newconfig = 'umask ' + term[target_filename]
		print newconfig	#正确值

		with open(target_filename,"a+") as f:
			f.write(newconfig + "\n")
		log.print_repaire_log(self.msg)


	def echo_data(self):
		print self.data

	def run(self):

		#self.echo_data()
		for term in self.data:	#遍历每个修改项
			#print term.keys()[0]    //返回PASS_MAX_DAYS
			level = self.verfiy(term)	#返回需要修复的等级，如更新、添加、无需修复
			#print level
			if self.isrepair==True:
				self.repair(term,level)


if __name__=='__main__':
	data = [{'update': '027', './target_file/profile': '027'}, 
			{'update': '027', './target_file/csh.login': '027'}, 
			{'update': '027', './target_file/csh.cshrc': '027'}, 
			{'update': '027', './target_file/bashrc': '027'}]
	isrepair=False
	bashrc = Pass(data,isrepair)
	bashrc.run()
