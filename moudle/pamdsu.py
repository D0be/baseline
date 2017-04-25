#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re       # 导入模块
import lib.log as log
import lib.backup as backup



class Pass(object):    
	"""docstring for Pass"""
	def __init__(self, data,isrepair):		
		self.data=data
		self.isrepair= isrepair
		self.target_filename = "./target_file/pam.d_su"
		self.msg = ''
	
	def verfiy(self,i):
		f=open(self.target_filename,"r")
		data= f.read()
		f.close()
		r= 0
		for n in i:
			if n != 'update':
				str= n

		patt = r'auth\s+sufficient\s+/lib/security/pam_rootok.so\nauth\s+required\s+/lib/security/pam_wheel.so\s+group=wheel\n' 
		m = re.search(patt,data)
		# print i[str]
		# print m.group(0)
		if m:
		 	pass
		else:
			r=2
			print "no config"
		self.msg = self.target_filename+'=> project: '+str
		log.print_check_log(self.msg,r)
		return r



	def repair(self,i,r):			
		if  r==0:					
			log.print_check_log(self.msg+' Don\'t need repair .Because it' ,0)
		elif r==1:					
			self.addConfig(i)
		else:						
			log.print_check_log('Error',2)	



	def addConfig(self,i):		
		f = open(self.target_filename, "r")
		data=f.read()
		print data
		f.close()
		data1 = i['update']+data
		print data1
		f = open(self.target_filename, "w")
		f.write(data1)
		f.close()
		log.print_repaire_log(self.msg)

	def run(self):		
		backup.moveFileto(self.target_filename)
		for i in self.data:	  
			# print i
			pair=self.verfiy(i)	
			# print pair
			if self.isrepair == True:		
				self.repair(i,pair)    


if __name__ == '__main__':
	# data =[{'update': '90', 'PASS_MAX_DAYS': '90'}, {'PASS_MIN_DAYS': '0', 'update': '0'}, {'PASS_MIN_LEN': '8', 'update': '8'}]
	data = [{'su': '', 'update': 'auth    sufficient   /lib/security/pam_rootok.so\nauth    required    /lib/security/pam_wheel.so group=wheel\n '}]
	isrepair=False
	Pass=Pass(data,isrepair)
	Pass.run()