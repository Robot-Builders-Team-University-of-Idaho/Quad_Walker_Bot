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
	setAngle(1, 110)
	setAngle(2, 240)
	setAngle(3, 140)
	time.sleep(0.5)
	setAngle(1, 180)
	setAngle(2, 180)
	setAngle(3, 90)
	time.sleep(0.5)

disableTorque(1)
disableTorque(2)
disableTorque(3)

closeServos()
