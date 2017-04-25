#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 导入模块
from optparse import OptionParser
import sys
import os
import re
import time


#设置命令行参数 -r -f
parser =OptionParser()
parser.add_option("-f", "--file", action="store",type="string",dest="filename",
	help="write file")
parser.add_option("-t", "--threads",action="store",type="int",dest="threads",default=5,
	help="setting thread quantity")
parser.add_option("-r" ,"--repair ", action="store_true",dest="repair", default="False",
	help="Are you repair file ?")
(options,args) = parser.parse_args()

#判断命令行输入的文件名是否为空
if options.filename.strip()=="":
	print "please input filename"
	parser.print_help()
	sys.exit()
elif not os.path.exists(options.filename.strip()): #判断文件名是否存在 
	print "File not exits"
	sys.exit()

print '''
 __  __       _            _   ____         __        __   _ ____        
|  \/  | __ _| | _____  __| | | __ ) _   _  \ \      / /__(_) __ )  ___  
| |\/| |/ _` | |/ / _ \/ _` | |  _ \| | | |  \ \ /\ / / _ \ |  _ \ / _ \ 
| |  | | (_| |   <  __/ (_| | | |_) | |_| |   \ V  V /  __/ | |_) | (_) |
|_|  |_|\__,_|_|\_\___|\__,_| |____/ \__, |    \_/\_/ \___|_|____/ \___/ 
                                     |___/ 
	
'''
print 'The python code will run .... Please wait few time'
time.sleep(2)















# 加载配置文件的函数  以特定格式输出  字典{数组[字典{"":"","update":""}]}
def loadfile(filename):
	d=dict()	#定义大字典
	l=[]		#定义初始数组为空
	with open(filename) as f:  #打开文件
		for line in f.readlines():	#一行一行的输出文件内容
			tye,check,update = line.split('|')  # 以 | 分割每行内容 tye （要修改的系统文件名，对象） check（检查项） update（更新后的数据） 
			key,value = check.split(':')  #以 : 分割check 内容 key：value
			tmp = {key : value,'update' : update.strip('\n') }  # 以字典形式组合check 内容 并过滤掉 '\n'
			if not d.has_key(tye):  # 判断键是否存在
				d[tye] = []			# 不存在则赋为空数组
			d[tye].append(tmp)		#存在 则追加
		return    d			#返回大字典
				 
				

#设置启动函数
def start(isrepair,data):
	i=0 
	for key in data:
		time.sleep(0.5)  
		i=i+1
		print 'Checking for ' + str(i) + ' running'
		exec 'import moudle.'+key+ ' as load'	
		# print key
		Passa=load.Pass(data[key],isrepair)	
		Passa.run()					#运行函数



data=loadfile(options.filename)
# print data   # 获取配置文件内容
start(options.repair,data)	
# print data
# 
