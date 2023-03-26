from robot_parts.servos import *

if not servo.connect():
	quit()

for i in range(1, 13):
	a = servo(i)
	a.torqueOff()

servo.close()
