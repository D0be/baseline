#!/usr/bin/python
# -*- coding: GBK -*-
import re       # ����ģ��
import lib.log as log
import lib.backup as backup



class Pass(object):    #������
	"""docstring for Pass"""
	def __init__(self, data,isrepair):		#���캯��   data  ���������   isrepair �Ƿ��޸� ��True ��False��
		self.data=data
		self.isrepair= isrepair
		self.target_filename = "./target_file/passwd"
		self.msg = ''

	def repair(self):
		print "can't repair"
		
	
	def verfiy(self,i):			
		f=open(self.target_filename,"r")		#���ļ�			#��ȡ�ļ�����
		r= 0
		tmp = 1
		while True:
			line = f.readline()
			if not line:
				break
			line_list = line.split(":")
			#print line_list
			if line_list[0] != "root" and line_list[2] =="0":
				print "�û�����%s��UIDΪ0���뽵Ȩ��" % line_list[0]
				tmp = 0
		if tmp == 1:
			print "�����ڳ���ROOT�û�֮��UIDΪ0���û������ϱ�׼"
		f.close()

	def run(self):
		backup.moveFileto(self.target_filename)
		self.verfiy('')



if __name__ == '__main__':
	data = [{'passwd': '', 'update': ''}]
	isrepair=False
	Passa=Pass(data,isrepair)	
	Passa.run()	
	




