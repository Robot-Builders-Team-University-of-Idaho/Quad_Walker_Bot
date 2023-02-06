from robot_parts.servos import *

initServos()

enableTorque(2)
enableTorque(3)

setAngle(2, 305)
setAngle(3, 150)

input("Press enter to throw:")

setAngle(2, 245)
#while getAngle(2) > 270:
	#time.sleep(0.000001)
setAngle(3, 110)

time.sleep(1)

setAngle(2, 180)
setAngle(3, 30)

disableTorque(2)
disableTorque(3)

closeServos()
