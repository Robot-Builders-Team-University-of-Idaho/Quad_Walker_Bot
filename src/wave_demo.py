from robot_parts.servos import *
import time

# initialize servo control
# if it fails, quit the program
if not servo.connect():
	quit()

a = servo(1)
b = servo(2)
c = servo(3)

for i in range(0, 5):
	a.setAngle(110)
	b.setAngle(240)
	c.setAngle(140)
	time.sleep(0.5)
	a.setAngle(180)
	b.setAngle(180)
	c.setAngle(90)
	time.sleep(0.5)

closeServos()
