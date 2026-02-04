#coding=gbk

import threading
import DobotDllType as dType
import math
import time

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
		# pos = dType.GetPose(api)
		dType.SetPTPJointParams(api, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 0)
		dType.SetPTPCommonParams(api, 1000, 1000, 0)
		# xr = pos[0]
		# yr = pos[1]
		# zr = pos[2]
		# rail=dType.GetPoseL(api)
		dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 35, 250, 20, 0, 0)
		#dType.SetPTPWithLCmd(api, dType.PTPMode.PTPMOVLXYZMode, 35, 250, 20, 0, rail[0], 0)
#######################################################

charw=raw_input("输入汉字：")
dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 35, 250, -85, 0,  0)

time.sleep(2)

if (charw=='一'):
#if 1:
	dType.SetWAITCmd(api, 1000, 0)
	pos = dType.GetPose(api)
	xr = pos[0]
	yr = pos[1]
	zr = pos[2]
	print('x=%3.0f,y=%3.0f,z=%3.0f' %(xr,yr,zr))
	raw_input("Go ahead")
#	dType.SetQueuedCmdClear(api)
	dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, xr-40, yr-3, zr, 0, 1)
	dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, xr-40, yr-3, zr+5, 0, 1)
	dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, xr-20, yr+50, zr+5, 0, 1)
	dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, xr-20, yr, zr, 0, 1)
	dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, xr-20, yr-60, zr, 0, 1)	
		
############### Input PTP   ##############
# while 1:

	# x = input("Please input x:") 
	# y = input("Please input y:") 
	# z = input("Please input z:") 
	# l = input("Please input l:") 

	# dType.SetPTPWithLCmd(api, dType.PTPMode.PTPMOVLXYZMode, x, y, z, 0, l, 0)
###########################################
time.sleep(2)
dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 35, 250, 20, 0, 0)
#dType.SetQueuedCmdStartExec(api)

dType.DisconnectDobot(api)
exit()

