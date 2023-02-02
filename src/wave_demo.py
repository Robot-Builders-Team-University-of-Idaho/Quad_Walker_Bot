from robot_parts.servos import *
import time

# initialize servo control
# if it fails, quit the program
if not initServos():
	quit()

enableTorque(1)
enableTorque(2)
enableTorque(3)

for i in range(0, 5):
	setAngle(1, 90)
	setAngle(2, 270)
	setAngle(3, 180)
	time.sleep(1)
	setAngle(1, 180)
	setAngle(2, 180)
	setAngle(3, 90)

disableTorque(1)
disableTorque(2)
disableTorque(3)

closeServos()
