#coding=gbk

import threading
import DobotDllType as dType
import math
import time
import string

CON_STR = {
    dType.DobotConnect.DobotConnect_NoError:  "DobotConnect_NoError",
    dType.DobotConnect.DobotConnect_NotFound: "DobotConnect_NotFound",
    dType.DobotConnect.DobotConnect_Occupied: "DobotConnect_Occupied"}

#Load Dll
api = dType.load()

#Connect Dobot
state = dType.ConnectDobot(api, "", 115200)[0]
print("Connect status:",CON_STR[state])

if (state == dType.DobotConnect.DobotConnect_NoError):
		dType.SetQueuedCmdClear(api)		
		dType.SetPTPJointParams(api, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 0)
		dType.SetPTPCommonParams(api, 1000, 1000, 0)		
		dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 200, 0, 20, 0, 0)
		time.sleep(2)
		pos = dType.GetPose(api)
		xr = pos[0]
		yr = pos[1]
		zr = pos[2]
		#rail=raw_input("Please initialize the Rail position:")
		rail=dType.GetPoseL(api)
		dType.SetPTPWithLCmd(api, dType.PTPMode.PTPMOVLXYZMode, 200, 0, 20, 0, rail[0], 0)
else:
	raw_input("Press Enter to continue...")
	exit()
time.sleep(2)
dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 200, 0, 20, 0, 0)
############### Input PTP   ##############
while 1:
	x=y=z=0
	x = input("Please input x:") 
	y = input("Please input y:")
	pos = dType.GetPose(api)
	xr = pos[0]
	yr = pos[1]
	#z = input("Please input z:") 
	#l = input("Please input l:") 
	if zr>=0:
		#lastIndex=dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, eval('x+xr'), eval('y+yr'), zr, 0, 0)
		lastIndex=dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, x, y, zr, 0, 0)
		zr=-4
		time.sleep(2)
	dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, x, y, eval('z+zr'), 0, 0)
	# dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, eval('x+xr'), eval('y+yr'), eval('z+zr'), 0, 0)
###########################################
time.sleep(2)
dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 200, 0, 20, 0, 0)
#dType.SetQueuedCmdStartExec(api)

dType.DisconnectDobot(api)
exit()

