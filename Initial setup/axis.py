#coding=gbk

import threading
import DobotDllType as dType
import math

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
		file_object = open('thefile.txt', 'w')
else:
	raw_input("Press Enter to continue...")
	exit()

get_flag=5
		
############### Input PTP   ##############
while (get_flag):
	pos = dType.GetPose(api)
	xr = pos[0]
	yr = pos[1]
	zr = pos[2]
	rail=dType.GetPoseL(api)
	print('x=%3.0f,y=%3.0f,z=%3.0f,l=%3.0f' %(xr,yr,zr,rail[0]))
	m=raw_input("Press Enter to continue...\n")
	file_object.write('%3.0f,%3.0f,%3.0f\n' %(xr,yr,zr))
	if(m=='x'):
		get_flag=0
###########################################

file_object.close( )
dType.DisconnectDobot(api)
exit()

