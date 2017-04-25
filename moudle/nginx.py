#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re       # 导入模块
import lib.log as log
import lib.backup as backup


#修改nginx的运行账户为nobody

class Pass(object):    #定义类
	"""docstring for Pass"""
	def __init__(self, data,isrepair):		#构造函数   data  传入的数组   isrepair 是否修复 （True ，False）
		self.data=data
		self.isrepair= isrepair
		self.target_filename = "./target_file/nginx.conf"
		self.msg = ''
		
	


	def repair(self,i,r):			#传过来 i r    根据r的值 来确定安全情况 以及如何修复
		if  r==1:					# r==0  存在不安全  需要编辑配置文件
			self.editConfig(i)

		elif r==2:					# r==2   没有配置选项   需要增加一个
			self.addConfig(i)

		elif r==0:					# r==1   安全 无须 修复
			log.print_check_log(self.msg+' Don\'t need repair .Because it' ,0)
		else:						# 其他值 则报错
			log.print_check_log('Error',2)


	
	def verfiy(self,i):
		f=open(self.target_filename,"r")
		data= f.read()
		f.close()
		r= 0
		for n in i:						# i 传过来的数组内容  遍历 n（i 的key）
			if n !=	'update':			# 如果 n 不为 update   
				str = n
		patt = r'\n%s.*?(\w+);' % (str)
		m = re.search(patt,data)
		#print m.group(1)
		if m:
			if m.group(1) != 'nobody':
				r=1
			else:
				pass
		else:
			r=2
		self.msg = self.target_filename+'=> project: '+str
		log.print_check_log(self.msg,r)
		return r						#	返回 r



	def addConfig(self,i):		#添加配置选项的函数
		f = open(self.target_filename, "r")
		data=f.read()
		f.close()
		# for n in i:						# i 传过来的数组内容  遍历 n（i 的key）
		# 	if n !=	'update':			# 如果 n 不为 update   
		# 		str = n		
		#patt = r'\n%s.*?(\w+);' % (str)
		#m = re.search(patt,data)
		n = data + '\nuser nobody;\n'
		f = open(self.target_filename, "w")
		f.write(n)
		f.close()
		log.print_repaire_log(self.msg)

	def editConfig(self,i):			#编辑配置文件
		f =open(self.target_filename,"r")
		data=f.read()
		f.close()
		for n in i:						# i 传过来的数组内容  遍历 n（i 的key）
			if n !=	'update':			# 如果 n 不为 update   
				str = n
		patt = r'\n%s.*?(\w+);' % (str)
		m= re.search(patt,data)
		print m.group(1)
		data = re.sub(patt,'\nuser nobody;',data)
		f=open(self.target_filename,"w")
		f.write(data)
		f.close()
		log.print_repaire_log(self.msg)


	

	def run(self):		#运行函数
		backup.moveFileto(self.target_filename)	
		for i in self.data:	  #遍历 数组中的每个小字典
			# print i
			pair=self.verfiy(i)	
			# print pair#将验证的返回值赋给一个变量
			if self.isrepair == True:		# 如果 isrepair为True  （就是说要修复配置文件，命令行参数 写了 -r）
				self.repair(i,pair)    # 运行修复函数


if __name__ == '__main__':
	# data =[{'update': '90', 'PASS_MAX_DAYS': '90'}, {'PASS_MIN_DAYS': '0', 'update': '0'}, {'PASS_MIN_LEN': '8', 'update': '8'}]
	data = [{'user': 'nobody', 'update': 'nobody'}]
	isrepair=True
	Pass=Pass(data,isrepair)
	Pass.run()
