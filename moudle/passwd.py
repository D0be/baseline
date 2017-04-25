#!/usr/bin/python
# -*- coding: GBK -*-
import re       # 导入模块
import lib.log as log
import lib.backup as backup



class Pass(object):    #定义类
	"""docstring for Pass"""
	def __init__(self, data,isrepair):		#构造函数   data  传入的数组   isrepair 是否修复 （True ，False）
		self.data=data
		self.isrepair= isrepair
		self.target_filename = "./target_file/passwd"
		self.msg = ''

	def repair(self):
		print "can't repair"
		
	
	def verfiy(self,i):			
		f=open(self.target_filename,"r")		#打开文件			#读取文件内容
		r= 0
		tmp = 1
		while True:
			line = f.readline()
			if not line:
				break
			line_list = line.split(":")
			#print line_list
			if line_list[0] != "root" and line_list[2] =="0":
				print "用户名：%s的UID为0，请降权限" % line_list[0]
				tmp = 0
		if tmp == 1:
			print "不存在除了ROOT用户之外UID为0的用户，符合标准"
		f.close()

	def run(self):
		backup.moveFileto(self.target_filename)
		self.verfiy('')



if __name__ == '__main__':
	data = [{'passwd': '', 'update': ''}]
	isrepair=False
	Passa=Pass(data,isrepair)	
	Passa.run()	
	




