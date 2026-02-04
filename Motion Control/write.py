#coding=gbk

import threading
import DobotDllType as dType
import math
import time
import string

import write_1

CON_STR = {
    dType.DobotConnect.DobotConnect_NoError:  "DobotConnect_NoError",
    dType.DobotConnect.DobotConnect_NotFound: "DobotConnect_NotFound",
    dType.DobotConnect.DobotConnect_Occupied: "DobotConnect_Occupied"}

	
# def liftpen(pose):
		# xr = pose[0]
		# yr = pose[1]
		# zr = int(pose[2])
		# dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, int(xr), int(yr), int(zr+10), 0, 0)
	
#Load Dll
api = dType.load()

#Connect Dobot
state = dType.ConnectDobot(api, "", 115200)[0]
print("Connect status:",CON_STR[state])

if (state == dType.DobotConnect.DobotConnect_NoError):
		dType.SetQueuedCmdClear(api)		
		dType.SetPTPJointParams(api, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 0)
		dType.SetPTPCommonParams(api, 1000, 1000, 0)	
else:
	raw_input("Press Enter to continue...")
	exit()
dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 200, 0, 20, 0, 0)
time.sleep(2)
############ First Pen Down ############
file="牧.txt"
f=open(file,"r")
content=f.readlines()	#


write_1.penwrite(content)


# dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 200, 0, -4, 0, 1)
# step=0

# for i in range(step,len(content)):
	# if content[i]=="s\n":
		# step=i
	# else:
		# continue
	# for i in range(step):
		# pos = dType.GetPose(api)
		# xr = int(pos[0])
		# yr = int(pos[1])
		# zr = int(pos[2])
		# x=int(content[i].split()[0])
		# y=int(content[i].split()[1])
		# lastIndex=dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, eval('x+xr'), eval('y+yr'), zr, 0, 1)
		# dType.SetQueuedCmdStartExec(api)
		# while lastIndex > dType.GetQueuedCmdCurrentIndex(api)[0]:
			# time.sleep(1)
		# dType.SetQueuedCmdStopExec(api)
		# liftpen(pos)
		# step+=1
# for i in range(len(content)):
	# if content[i]=="s\n":
		# liftpen(dType.GetPose(api))
	# else:
		# pos = dType.GetPose(api)
		# xr = int(pos[0])
		# yr = int(pos[1])
		# zr = int(pos[2])
		# x=int(content[i].split()[0])
		# y=int(content[i].split()[1])
		# lastIndex=dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, x+xr, y+yr, zr, 0, 1)
# dType.SetQueuedCmdStartExec(api)
# while lastIndex > dType.GetQueuedCmdCurrentIndex(api)[0]:
	# time.sleep(1)
# dType.SetQueuedCmdStopExec(api)

	
	
	



dType.DisconnectDobot(api)
exit()
