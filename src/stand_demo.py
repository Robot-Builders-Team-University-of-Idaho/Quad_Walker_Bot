from robot_parts.legs import *
import time

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
	legs[i].b.setAngle(200)
	legs[i].c.setAngle(150)

#time.sleep(0.5)
for i in range(leg_count):
	legs[i].b.waitForAngle(200)
	legs[i].c.waitForAngle(150)

# make jobo stand up a bit taller
for i in range(leg_count):
	legs[i].b.setAngle(150)

#time.sleep(0.5)
for i in range(leg_count):
	legs[i].b.waitForAngle(150)

# make jobo twist back and forth a few times
for i in range(5):
	for i in range(leg_count):
		legs[i].a.setAngle(150)
	
	#time.sleep(0.5)
	for i in range(leg_count):
		legs[i].a.waitForAngle(150)
	
	for i in range(leg_count):
		legs[i].a.setAngle(210)
	
	#time.sleep(0.5)
	for i in range(leg_count):
		legs[i].a.waitForAngle(210)

servo.close()
