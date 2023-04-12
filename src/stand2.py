from robot_parts.legs import *
import time
from datetime import datetime
import math as m
from utils.movements import *


servo.connect()

# initialize legs and servos
leg_count = 4
legs = []
for i in range(leg_count):
	n = i * 2 + i + 1
	legs.append(leg(n, n+1, n+2))

# set all joints to straight
for i in range(leg_count):
	legs[i].a.setAngle(180)
	legs[i].b.setAngle(180)
	legs[i].c.setAngle(180)

#time.sleep(0.5)
for i in range(leg_count):
	legs[i].a.waitForAngle(180)
	legs[i].b.waitForAngle(180)
	legs[i].c.waitForAngle(180)

# make jobo stand up
for i in range(leg_count):
	legs[i].b.setAngle(235)
	legs[i].c.setAngle(90)
	
for i in range(leg_count):
	legs[i].b.waitForAngle(235)
	legs[i].c.waitForAngle(90)

# make jobo stand up
for i in range(leg_count):
	legs[i].b.setAngle(150)
	legs[i].c.setAngle(160)

time.sleep(2)

servo.close()
