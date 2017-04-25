#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import sys

class Pass(object):
	"""chmod passwd/shadow/group"""

	def __init__(self,data,isrepair):
		self.data = data
		self.isrepair= isrepair


		
	def repair(self,term):
		#os.system("echo \"aaaaaaa\"")

		for n in term:						# i 传过来的数组内容  遍历 n（i 的key）
			if n !=	'update':			# 如果 n 不为 update   
				str = n

		#print str,term[str]
		ch = 'chmod ' + term['update'] + ' ' + str
		print ("修改%s权限为%s") % (str,term[str])
		os.system(ch)

	def echo_data(self):
		print self.data

	def run(self):
		#self.echo_data()
		for term in self.data:	#遍历每个修改项
			if self.isrepair==True:
				self.repair(term)


if __name__=='__main__':
	data = [{'update': '644','./target_file/passwd': '644'}, 
			{'update': '600','./target_file/shadow': '600'}, 
			{'update': '644','./target_file/group': '644'}]
	isrepair=True
	Pass=Pass(data,isrepair)
	Pass.run()
