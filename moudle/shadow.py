#!/usr/bin/python
# -*- coding: GBK -*-
import re       # ����ģ��
import lib.backup as backup
import time


class Pass(object):    #������
	"""docstring for Pass"""
	def __init__(self, data,isrepair):		#���캯��   data  ���������   isrepair �Ƿ��޸� ��True ��False��
		self.data=data
		self.isrepair= isrepair
		self.target_filename = "./target_file/shadow"

	def repair(self):
		print "fliname :shadow"
		print 'no repair'
		
	
	def verfiy(self,i):					# ��֤����  
		f=open(self.target_filename,"r")		#���ļ�			#��ȡ�ļ�����
		r= 0
		while True:
			line = f.readline()
			if not line:
				break
			line_list = line.split(":")
			if line_list[1] =="*" :
				time.sleep(0.3)
				print "�û�����%s�ǿ���������������" % line_list[0]


	def run(self):		#���к���
		backup.moveFileto(self.target_filename)
		self.verfiy('')	#����֤�ķ���ֵ����һ������


if __name__ == '__main__':
	data = [{'passwd': '', 'update': ''}]
	isrepair=False
	Passa=Pass(data,isrepair)	
	Passa.run()	
	


