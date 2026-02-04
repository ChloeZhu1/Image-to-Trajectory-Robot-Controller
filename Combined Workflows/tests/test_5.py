import time
import threading
import DobotDllType as dType


def getpos():
	pos = dType.GetPose(api)
	xr = int(pos[0])
	yr = int(pos[1])
	zr = int(pos[2])
	return xr,yr,zr

def waitstop():
	dType.SetQueuedCmdStartExec(api)
	while lastIndex[0] > dType.GetQueuedCmdCurrentIndex(api)[0]:
		dType.dSleep(100)
	dType.SetQueuedCmdStopExec(api)
	dType.SetQueuedCmdClear(api)
	
# global point
# point=0
def getdy():
	fd=open("E:\\camera\\point.txt","r+")
	context=fd.read()
	try:
		point=int(context.split()[0])
	except (IndexError),dy:
		point=0
		pass
	fd.close()
	delta=point-100
	return delta
api = dType.load()
CON_STR = {
    dType.DobotConnect.DobotConnect_NoError:  "DobotConnect_NoError",
    dType.DobotConnect.DobotConnect_NotFound: "DobotConnect_NotFound",
    dType.DobotConnect.DobotConnect_Occupied: "DobotConnect_Occupied"}
state = dType.ConnectDobot(api, "", 115200)[0]

if (state == dType.DobotConnect.DobotConnect_NoError):
	dType.SetQueuedCmdClear(api)
	# dType.SetPTPJointParams(api,100,100,100,100,100,100,100,100)
	dType.SetPTPCoordinateParams(api,10000,200,100,100)
	# dType.SetPTPJumpParams(api, 10, 100)
	dType.SetPTPCommonParams(api, 1000, 100)
	dType.SetPTPLParams(api, 400, 100, 0)
	
while (True):
	dy=getdy()
	lastIndex = dType.SetPTPWithLCmd(api, dType.PTPMode.PTPMOVLXYZMode, dType.GetPose(api)[0]+dy/10, dType.GetPose(api)[1], dType.GetPose(api)[2], 0, dType.GetPoseL(api)[0] , 1)
	waitstop()
	dy=0
	time.sleep(0.1)