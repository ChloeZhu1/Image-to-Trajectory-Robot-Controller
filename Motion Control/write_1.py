#coding=gbk

import re
import time
import threading
import DobotDllType as dType
api = dType.load()

deepth=-4

def getpos():
	pos = dType.GetPose(api)
	xr = int(pos[0])
	yr = int(pos[1])
	zr = int(pos[2])
	return xr,yr,zr

# def findSubStr(substr, str, i):  
	# count = 0  
	# while i > 0:                  
		# index = str.find(substr)  
		# if index == -1:  
			# return -1  
		# else:  
			# str = str[index+1:]   
			# i -= 1  
			# count = count + index + 1  
	# return count  
def findSubStr(key,str,i):
	index=str.index(key)
	if i<=1:
		return index
		print index
	for j in range(i-1):
		index = str.index(key,index+1)
    # if index==-1:
        # break
	return index
	
def penwrite(trace):
	global k
	k=1
	# for i in range(trace.count("s\n")-1):
		# xr,yr,zr=getpos()
		# xr=200
		# yr=0
		# zr=20
		# print trace[findSubStr("s\n",trace,i+1)+1].split()[0]
		# x=int(trace[findSubStr("s\n",trace,i+1)+1].split()[0])
		# y=int(trace[findSubStr("s\n",trace,i+1)+1].split()[1])
		
		# 移动到固定位置
		# dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,x+xr,y+yr,zr,1)
			# 向下
		# xr,yr,zr=getpos()
		# dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,xr,yr,-4,1)
			# 写字
		# for i in range(k,len(trace)):
			# if trace[i]=="s\n":
				# 提笔
				# xr,yr,zr=getpos()
				# lastIndex=dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,xr+x,yr+y,20,1)
				# k=i+1
				# break			
			# print trace[i].split()[0]
			# x=int(trace[i].split()[0])
			# y=int(trace[i].split()[1])
			# dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,200+x,y,-4,0,1)
	x=[0 for n in range(len(trace))]
	y=[0 for n in range(len(trace))]		
	for i in range(k,len(trace)):
		if trace[i]=="s\n":
			break
		x[i-1]=int(trace[i].split()[0])
		
		y[i-1]=int(trace[i].split()[1])
		#print (x[i],y[i])
	print x[x.index(0)-1]
	xr,yr,zr=getpos()
	dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,x[0]+xr,y[0]+yr,zr,1)
	#time.sleep(1)
	dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,x[0]+xr,y[0]+yr,deepth,1)
	#time.sleep(1)
	# dType.SetQueuedCmdStartExec(api)
	# time.sleep(1)
	# dType.SetQueuedCmdStopExec(api)
	
	for i in range(x.index(0)-1):
		lastIndex=dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,x[i]+xr,y[i]+yr,deepth,1)
		# print dType.GetQueuedCmdCurrentIndex(api)[0]
		print x[i]+xr,y[i]+yr
		print (lastIndex)
		# time.sleep(0.5)
	#time.sleep(1)
	while lastIndex[0] > dType.GetQueuedCmdCurrentIndex(api)[0]:
		dType.dSleep(100)
	dType.SetQueuedCmdStopExec(api)	
	xr,yr,zr=getpos()
	
	dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,xr,yr,20,0,0)
	# print ("set")
	# time.sleep(0.1)
	
	# dType.SetQueuedCmdStartExec(api)

	# time.sleep(2)
	# dType.SetQueuedCmdStopExec(api)	