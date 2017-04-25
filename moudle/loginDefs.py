#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re       # 导入模块
import lib.log as log
import lib.backup as backup


class Pass(object):    #定义类
	"""docstring for Pass"""
	def __init__(self, data,isrepair):		#构造函数   data  传入的数组   isrepair 是否修复 （True ，False）
		self.data=data
		self.isrepair= isrepair
		self.target_filename = "./target_file/login.defs"
		self.msg = ''
		
	


	def repair(self,i,r):	
		if  r==1:					
			self.editConfig(i)
		elif r==2:					
			self.addConfig(i)
		elif r==0:					
			log.print_check_log(self.msg+' Don\'t need repair .Because it' ,0)
		else:						
			log.print_check_log('Error',2)


	
	def verfiy(self,i):					
		f=open(self.target_filename,"r")		
		data= f.read()	
		f.close()					
		r= 0							
		for n in i:					
			if n !=	'update':			 
				str = n
				# print n 
		patt = r'(%s)(.*?)(\d+)' % str	
		#print patt
		m = re.search(patt,data)   		# 匹配文件中的所要修改的内容
		# print m.group(3)				# 
		# print i[str]
		if m:							# 如果匹配成功
			if int(m.group(3)) > int(i[str]):	#判断安全的标准  每个文件的都不一样
				r=1
			else:
				pass					#给r一个新值

		else:
			r=2
		self.msg = self.target_filename+'=> project: '+str
		log.print_check_log(self.msg,r)
		return r						#	返回 r



	def addConfig(self,i):		#添加配置选项的函数
		f = open(self.target_filename, "a+")
		for n in i:
			if n !=	'update':
				str = n
		f.write(str+'  '+i['update'] + "\n")
		f.close()
		log.print_repaire_log(self.msg)

	def editConfig(self,i):			#编辑配置文件
		f =open(self.target_filename,"r+")
		data=f.read()
		f.close()
		for n in i:
			if n !=	'update':
				str = n
		patt = r'(%s)(.*?)(\d+)' % str
		data = re.sub(patt,i['update'],data)
		f=open(self.target_filename,"w")
		f.write(data)
		f.close
		log.print_repaire_log(self.msg)



	

	def run(self):	
		backup.moveFileto(self.target_filename)	
		for i in self.data:	  #遍历 数组中的每个小字典
			#print i
			pair=self.verfiy(i)	#将验证的返回值赋给一个变量
			if self.isrepair == True:		# 如果 isrepair为True  （就是说要修复配置文件，命令行参数 写了 -r）
				self.repair(i,pair)    # 运行修复函数



if __name__ == '__main__':
	data =[{'update': '90', 'PASS_MAX_DAYS': '90'}, {'PASS_MIN_DAYS': '0', 'update': '0'}, {'PASS_MIN_LEN': '8', 'update': '8'}]
	isrepair=True
	Pass=Pass(data,isrepair)
	Pass.run()



