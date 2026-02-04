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

    #Clean Command Queued
    dType.SetQueuedCmdClear(api)

    #Async Motion Params Setting
dType.SetPTPJointParams(api,200,200,200,200,200,200,200,200)
dType.SetPTPCoordinateParams(api,200,200,200,200)
dType.SetPTPJumpParams(api, 10, 200)
dType.SetPTPCommonParams(api, 100, 100)
moveX=0;moveY=0;moveZ=10;moveFlag=-1
pos = dType.GetPose(api)
x = pos[0]
y = pos[1]
z = pos[2]
rHead = pos[3]
Flag=5
lastIndex = dType.SetPTPWithLCmd(api, dType.PTPMode.PTPMOVLXYZMode, dType.GetPose(api)[0], dType.GetPose(api)[1], dType.GetPose(api)[2], 0, 500, 1)
#Start to Execute Command Queued
dType.SetQueuedCmdStartExec(api)

    #Wait for Executing Last Command 
while lastIndex[0] > dType.GetQueuedCmdCurrentIndex(api)[0]:
    print lastIndex,dType.GetQueuedCmdCurrentIndex(api)[0]
    dType.dSleep(100)

    #Stop to Execute Command Queued
dType.SetQueuedCmdStopExec(api)

#Disconnect Dobot
dType.DisconnectDobot(api)
