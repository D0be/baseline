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
		self.target_filename = "./target_file/ssh_config"
		self.msg = ''

		
	


	def repair(self,i,r):
		if  r==1:					
			self.editConfig(i)
			print " repair success"
		elif r==2:					
			self.addConfig(i)
			print "repair success"
		elif r==0:					
			print "no repaire"
		else:						
			print "Error"


	
	def verfiy(self,i):
		f=open(self.target_filename,"r")
		data= f.read()
		f.close()
		r= 0
		for n in i:
			if n != 'update':
				str=n
		# print str
		patt = r'(%s)( *)(.*)' % str
		m = re.search(patt,data)
		# print i[str]
		# print m.group()
		if m:
			if  m.group(3) != i[str] :
				r=1
			elif m.group(3) == i[str]:
				pass
		else:
			r=2
		self.msg = self.target_filename+'=> project: '+str
		log.print_check_log(self.msg,r)
		return r
		



	def addConfig(self,i):		
		f = open(self.target_filename, "a+")
		for n in i:
			if n != 'update':
				str = n
		f.write(str + ' '+i['update']+'\n')
		f.close()
		log.print_repaire_log(self.msg)
		
	def editConfig(self,i):			
		f =open(self.target_filename,"r")
		data=f.read()
		f.close()
		for n in i:
			if n != 'update':
				str = n
		patt = r'(%s)( *)(.*)' % str
		m= re.search(patt,data)
		# print m.group()
		data = re.sub(patt,str+' '+i['update'],data)
		f=open(self.target_filename,"w")
		f.write(data)
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
	data = [{'PermitRootLogin': 'no', 'update': 'no'}]
	isrepair=False
	Pass=Pass(data,isrepair)
	Pass.run()
