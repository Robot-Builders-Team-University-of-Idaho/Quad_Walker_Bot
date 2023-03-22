from robot_parts.servos import *

if not servo.initServos():
	quit()

for i in range(1, 13):
	a = servo(i)
	a.disableTorque()

servo.closeServos()
