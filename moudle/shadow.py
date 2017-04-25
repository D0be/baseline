#!/usr/bin/python
# -*- coding: GBK -*-
import re       # 导入模块
import lib.backup as backup
import time


class Pass(object):    #定义类
	"""docstring for Pass"""
	def __init__(self, data,isrepair):		#构造函数   data  传入的数组   isrepair 是否修复 （True ，False）
		self.data=data
		self.isrepair= isrepair
		self.target_filename = "./target_file/shadow"

	def repair(self):
		print "fliname :shadow"
		print 'no repair'
		
	
	def verfiy(self,i):					# 验证函数  
		f=open(self.target_filename,"r")		#打开文件			#读取文件内容
		r= 0
		while True:
			line = f.readline()
			if not line:
				break
			line_list = line.split(":")
			if line_list[1] =="*" :
				time.sleep(0.3)
				print "用户名：%s是空密码请设置密码" % line_list[0]


	def run(self):		#运行函数
		backup.moveFileto(self.target_filename)
		self.verfiy('')	#将验证的返回值赋给一个变量


if __name__ == '__main__':
	data = [{'passwd': '', 'update': ''}]
	isrepair=False
	Passa=Pass(data,isrepair)	
	Passa.run()	
	


