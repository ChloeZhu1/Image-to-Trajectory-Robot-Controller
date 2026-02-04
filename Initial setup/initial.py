#coding=gbk

import threading
import DobotDllType as dType

CON_STR = {
    dType.DobotConnect.DobotConnect_NoError:  "DobotConnect_NoError",
    dType.DobotConnect.DobotConnect_NotFound: "DobotConnect_NotFound",
    dType.DobotConnect.DobotConnect_Occupied: "DobotConnect_Occupied"}
def initial():
	#Load Dll
	api = dType.load()

	#Connect Dobot
	state = dType.ConnectDobot(api, "", 115200)[0]
	print("Connect status:",CON_STR[state])

	if (state == dType.DobotConnect.DobotConnect_NoError):

		#Clean Command Queued
	dType.SetQueuedCmdClear(api)

		#Async Motion Params Setting
	dType.SetPTPJointParams(api,700,700,700,700,700,700,700,700)
	dType.SetPTPCoordinateParams(api,700,700,700,700)
	dType.SetPTPJumpParams(api, 10, 700)
	dType.SetPTPCommonParams(api, 100, 100)
