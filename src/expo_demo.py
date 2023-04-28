from robot_parts.legs import *
from datetime import datetime
import time
import sys

walk_cycles = 1
if len(sys.argv) > 0:
	try:
		walk_cycles = int(sys.argv[0])
	except:
		pass
	
	if walk_cycles < 0:
		raise ValueError("Argument to tell Jobo how many times to walk back and forth must be a positive integer")
		quit()

# define a and b joint high, low, and mid angles
a_low = 150
a_high = 210
b_low = 130
b_high = 210
b_mid = (b_high + b_low) / 2

# establish connection with servos
servo.connect()

# initialize legs and servos
leg_count = 4
legs = []
for i in range(leg_count):
	n = i * 2 + i + 1
	legs.append(leg(n, n+1, n+2))

# set all legs out straight and make sure all velocities are at max
for i in range(leg_count):
	legs[i].a.setVel(max_vel)
	legs[i].b.setVel(max_vel)
	legs[i].c.setVel(max_vel)
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
legs[1].a.setAngle(a_low)
legs[2].a.setAngle(a_high)
legs[3].a.setAngle(a_high)

# move b legs into stand up position
for i in range(leg_count):
	legs[i].b.setAngle(b_mid)

time.sleep(2)

start = datetime.now()
now = 0
speed = 50
#step_time = (1_000_000 * math.pi / 13_157.5) / (50 / 100)
step_time = 1_000_000
print(step_time)

# walk forward for a few steps
steps = 6.25
stop_time = step_time * steps
while now < stop_time:
	now = datetime.now() - start
	now = (now.seconds * 1_000_000) + now.microseconds
	legs[0].walk(True, False, now, speed=speed)
	legs[1].walk(True, True, now, speed=speed)
	legs[2].walk(False, True, now, speed=speed)
	legs[3].walk(False, False, now, speed=speed)

time.sleep(0.75)

# turn and then walk a few times
for i in range(walk_cycles):
	# set a joints to starting position for turning
	legs[0].a.setAngle(a_low)
	legs[1].a.setAngle(a_high)
	legs[2].a.setAngle(a_high)
	legs[3].a.setAngle(a_low)

	# move b legs into stand up position
	for i in range(leg_count):
		legs[i].b.setAngle(b_mid)

	time.sleep(0.75)

	start = datetime.now()
	now = 0

	# turn for a few steps
	steps = 4
	stop_time = step_time * steps
	while now < stop_time:
		now = datetime.now() - start
		now = (now.seconds * 1_000_000) + now.microseconds
		legs[0].walk(True, True, now, speed=speed)
		legs[1].walk(False, False, now, speed=speed)
		legs[2].walk(False, False, now, speed=speed)
		legs[3].walk(True, True, now, speed=speed)
	
	time.sleep(0.75)
	
	# set a joints into starting position for walking
	legs[0].a.setAngle(a_low)
	legs[1].a.setAngle(a_low)
	legs[2].a.setAngle(a_high)
	legs[3].a.setAngle(a_high)

	# move b legs into stand up position
	for i in range(leg_count):
		legs[i].b.setAngle(b_mid)
	
	time.sleep(0.75)

	start = datetime.now()
	now = 0

	# walk forward for a few steps
	steps = 6.25
	stop_time = step_time * steps
	while now < stop_time:
		now = datetime.now() - start
		now = (now.seconds * 1_000_000) + now.microseconds
		legs[0].walk(True, False, now, speed=speed)
		legs[1].walk(True, True, now, speed=speed)
		legs[2].walk(False, True, now, speed=speed)
		legs[3].walk(False, False, now, speed=speed)

# set jobo to standing position and lower c velocity
for i in range(leg_count):
	legs[i].a.setAngle(180)
	legs[i].b.setAngle(b_mid)
	legs[i].c.setVel(100)

time.sleep(0.75)

# make jobo lay down
for i in range(leg_count):
	legs[i].b.setAngle(180)
	legs[i].c.setAngle(180)

time.sleep(0.75)

# disable torque on all servos and set c velocity back to max
for i in range(leg_count):
	legs[i].a.torqueOff()
	legs[i].b.torqueOff()
	legs[i].c.torqueOff()
	legs[i].c.setVel(max_vel)

# close connection to servos
servo.close()
