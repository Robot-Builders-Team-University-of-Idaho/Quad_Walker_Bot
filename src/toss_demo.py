from robot_parts.servos import *
import time

servo.connect()

a = servo(2)
b = servo(3)

a.setAngle(305)
b.setAngle(150)

input("Press enter to throw:")

a.setAngle(245)
#while getAngle(2) > 270:
	#time.sleep(0.000001)
b.setAngle(110)

time.sleep(1)

a.setAngle(180)
b.setAngle(30)

servo.close()
