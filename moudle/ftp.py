#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import re
import time
import random
import os,sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
import lib.log as log
import lib.backup as backup



class Pass(object):
	"""password repair"""

	def __init__(self,data,isrepair):
		self.data = data
		self.isrepair = isrepair
		self.target_filename = "./target_file/vsftpd.conf"
		self.msg=' '

	def verfiy(self,term):#判断怎样修复，返回修复等级
		with open(self.target_filename,"r") as f:
			data= f.read()	#读取目标文件内容
			#print data
		for n in term:
			if n != 'update':
				str = n

		patt = r'(%s)=(\w{1,3})' % str		#正则
		# print patt
		m = re.search(patt,data)   		# 匹配文件中的所要修改的内容
		# print m.group(2)				#得到目标文件的值
		# print term['update']	#正确值
		
		if m:							# 如果匹配成功
			if m.group(2) == term['update']:	#判断安全的标准  每个文件的都不一样
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
		#self.backup()

		with open(self.target_filename,"r") as f:
			data= f.read()

		for n in term:
			if n != 'update':
				str = n

		newconfig = str + ' = ' + term['update'] + '\n'


		patt = r'(%s)=(\w{1,3})' % str
		#print patt

		data = re.sub(patt, newconfig, data)
		#print data
		with open(self.target_filename,"w+") as f:
			f.write(data+"\n")
		log.print_repaire_log(self.msg)

	def add_config(self,term):

		with open(self.target_filename,"r") as f:
			data= f.read()	#读取目标文件内容

		for n in term:
			if n != 'update':
				str = n

		newconfig = str + '=' + term['update']
		print newconfig	#正确值

		with open(self.target_filename,"a") as f:
			f.write(data + newconfig + "\n")

		log.print_repaire_log(self.msg)



	def echo_data(self):
		print self.data

	def run(self):
		backup.moveFileto(self.target_filename)	
		#self.echo_data()
		for term in self.data:	#遍历每个修改项
			#print term.keys()[0]    //返回PASS_MAX_DAYS
			level = self.verfiy(term)	#返回需要修复的等级，如更新、添加、无需修复
			print level
			if self.isrepair == True:
				self.repair(term,level)


if __name__=='__main__':
	data = [{'update': 'NO', 'anonymous_enable':'NO'},
			{'update': 'NO', 'no_anon_password':'NO'},
			{'update': 'NO', 'anon_upload_enable':'NO'},
			{'update': 'NO', 'anon_world_readable_only':'NO'},
			{'update': 'NO', 'anon_mkdir_write_enable':'NO'},
			{'update': 'NO', 'anon_other_write_enable':'NO'},
			{'update': 'NO', 'write_enable':'NO'},
			{'update': '022', 'local_umask':'022'},
			{'update': 'yes', 'userlist_enable':'yes'},
			{'update': 'no', 'userlist_deny':'no'},
			{'update': '300', 'idle_session_timeout':'300'},
			{'update': '120', 'data_connection_timeout':'120'},
			{'update': '60', 'ACCEPT_TIMEOUT':'60'},
			{'update': '60', 'connect_timeout':'60'},
			{'update': '200', 'Max_clients':'200'},
			{'update': '4', 'Max_per_ip':'4'}]
	isrepair = False
	passa = Pass(data,isrepair)
	passa.run()


