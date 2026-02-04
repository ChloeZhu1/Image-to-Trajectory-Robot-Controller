#coding=gbk
import threading
import DobotDllType as dType
import math
import re
import time
import string

global k
k=1
depth=-28

def getpos():
	pos = dType.GetPose(api)
	xr = int(pos[0])
	yr = int(pos[1])
	zr = int(pos[2])
	return xr,yr,zr

def findSubStr(key,str,i):
	index=str.index(key)
	if i<=1:
		return index
		print index
	for j in range(i-1):
		index = str.index(key,index+1)
	return index

def waitstop():
	dType.SetQueuedCmdStartExec(api)
	while lastIndex[0] > dType.GetQueuedCmdCurrentIndex(api)[0]:
		dType.dSleep(100)
	dType.SetQueuedCmdStopExec(api)
	dType.SetQueuedCmdClear(api)


api = dType.load()
CON_STR = {
    dType.DobotConnect.DobotConnect_NoError:  "DobotConnect_NoError",
    dType.DobotConnect.DobotConnect_NotFound: "DobotConnect_NotFound",
    dType.DobotConnect.DobotConnect_Occupied: "DobotConnect_Occupied"}
state = dType.ConnectDobot(api, "", 115200)[0]

if (state == dType.DobotConnect.DobotConnect_NoError):
	dType.SetQueuedCmdClear(api)
	# dType.SetPTPJointParams(api,100,100,100,100,100,100,100,100)
	dType.SetPTPCoordinateParams(api,2000,1000,100,100)
	# dType.SetPTPJumpParams(api, 10, 100)
	dType.SetPTPCommonParams(api, 1000, 100)
	dType.SetPTPLParams(api, 400, 100, 0)
	
# dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,140,0,20,0,1)
lastIndex = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,130,-50,20,0,1)
waitstop()
xr,yr,zr=getpos()
print xr,yr,zr
file="char\\秦.txt"
f=open(file,"r")
trace=f.readlines()
over=0
	
for j in range(trace.count("s\n")-1):
	x=[0 for n in range(len(trace))]
	y=[0 for n in range(len(trace))]
	for i in range(k+1,len(trace)):
		print i
		if trace[i]=="s\n":
			break
		print trace[i]
		x[i-k-1]=int(trace[i].split()[0])
		# print x[i-k-1]
		y[i-k-1]=int(trace[i].split()[1])
		if trace.index("s\n",k+1)+1==len(trace):
			over=1
	lastIndex = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,x[0]+xr,y[0]+yr,zr,0,1)
	waitstop()
	lastIndex = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,x[0]+xr,y[0]+yr,depth,0,1)
	waitstop()
	print ("\nNext\n")
	for i in range(x.index(0)):
		lastIndex = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,x[i]+xr,y[i]+yr,depth,0,1)
		print ("Axis")
		print i,x[i],y[i]
		waitstop()
		# if i=x.index(0)-2:
			# over=1
	if over==1:
		xr,yr,zr=getpos()
		lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, xr, yr, 20, 0, 1)
		waitstop()
	k=trace.index("s\n",k+1)
	dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,130,-50,20,0,1)
	lastIndex = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode,130,-50,20,0,1)
	waitstop()
	print("Done\n")

waitstop()
#dType.SetPTPLCmd(api.dType.PTPMOVLXYZMode,
	
dType.DisconnectDobot(api)

