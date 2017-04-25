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
		self.target_filename = "./target_file/fstab"
		self.msg = ''
		
	


	def repair(self,i,r):		
	
		if  r==0:					
			log.print_check_log(self.msg+' Don\'t need repair .Because it' ,0)
		elif r==2:					
			self.addConfig(i)
			print "repair success"
		else:						
			log.print_check_log('Error',2)


	
	def verfiy(self,i):
		f=open('C:\Users\L\Desktop\py\\target_file\\fstab',"r")
		data= f.read()
		f.close()
		r= 0
		for n in i:
			if n != 'update':
				str = n 
		patt = r'%s' % i[str] 
		m = re.search(patt,data)
		# print i[str]
	
		if m:
			pass
		else:
			r=2
		
		self.msg = self.target_filename+'=> project: '+str
		log.print_check_log(self.msg,r)
		return r		



	def addConfig(self,i):		
		f = open("C:\Users\L\Desktop\py\\target_file\\fstab", "a+")
		for n in i:
			if n != 'update':
				str = n
		f.write('\n'+i['update']+'\n')
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
	data = [{'tmp': '/tmp\s+/var/tmp\s+none\s+rw,noexec,nosuid,nodev,bind\s+0\s+0', 'update': '/tmp /var/tmp none rw,noexec,nosuid,nodev,bind 0 0'}]
	isrepair=True
	Pass=Pass(data,isrepair)
	Pass.run()
