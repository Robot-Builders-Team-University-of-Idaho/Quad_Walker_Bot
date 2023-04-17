from robot_parts.legs import *
from datetime import datetime
import time

# define a and b joint high, low, and mid angles
a_low = 150
a_high = 210
b_low = 110
b_high = 190
b_mid = (b_high + b_low) / 2

# establish connection with servos
servo.connect()

# initialize legs and servos
leg_count = 4
legs = []
for i in range(leg_count):
	n = i * 2 + i + 1
	legs.append(leg(n, n+1, n+2))

# set all legs out straight
for i in range(leg_count):
	legs[i].a.setAngle(180)
	legs[i].b.setAngle(180)
	legs[i].c.setAngle(180)

time.sleep(0.75)

# disable torque on b joint of each leg
for i in range(leg_count):
	legs[i].b.torqueOff()

# curl c joints in towards body to make it easier to stand up
for i in range(leg_count):
	legs[i].c.setAngle(90)

time.sleep(0.75)

# re-enable torque on b joints to stand up
for i in range(leg_count):
	legs[i].b.torqueOn()

# stand up making sure a joints for each leg are in correct start position
legs[0].a.setAngle(a_low)
legs[0].b.setAngle(b_mid)

legs[1].a.setAngle(a_high)
legs[1].b.setAngle(b_mid)

legs[2].a.setAngle(a_low)
legs[2].b.setAngle(b_mid)

legs[3].a.setAngle(a_high)
legs[3].b.setAngle(b_mid)

time.sleep(2)

start = datetime.now()
now = 0
speed = 25

# walk forward for 8 seconds
#while now < 8_000_000:
#	now = datetime.now() - start
#	now = (now.seconds * 1_000_000) + now.microseconds
#	legs[0].walk(True, now, speed=speed)
#	legs[1].walk(False, now, speed=speed)
#	legs[2].walk(True, now, speed=speed)
#	legs[3].walk(False, now, speed=speed)

# walk forward until ctrl + c is pressed
try:
	while True:
		now = datetime.now() - start
		now = (now.seconds * 1_000_000) + now.microseconds
		legs[0].walk(True, now, speed=speed)
		legs[1].walk(False, now, speed=speed)
		legs[2].walk(True, now, speed=speed)
		legs[3].walk(False, now, speed=speed)
except KeyboardInterrupt:
	print("\nCtrl + C Pressed... Stopping")

# disable torque on all servos
for i in range(leg_count):
	legs[i].a.torqueOff()
	legs[i].b.torqueOff()
	legs[i].c.torqueOff()

# close connection to servos
servo.close()
