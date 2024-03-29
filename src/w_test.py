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

legs[0].a.setAngle(180)
legs[0].b.setAngle(190)
legs[0].b.waitForAngle(190)

time_passed = 0
start_time = datetime.now()

while time_passed < 4_000_000: 
	time_passed = datetime.now() - start_time
	time_passed = (time_passed.seconds * 1_000_000) + time_passed.microseconds
	
	fl_angle_a = getSineAngle(time_passed, 135, 225, 180, True, 25) #(lower angle, upper angle, start angle, %speed)
	fr_angle_a = getSineAngle(time_passed, 135, 225, 135, True, 25)
	bl_angle_a = getSineAngle(time_passed, 135, 225, 225, True, 25)
	br_angle_a = getSineAngle(time_passed, 135, 225, 180, True, 25)
	
	fl_angle_b = getSineAngle(time_passed, 150, 190, 190, True, 25)
	mid = (190 - 150) / 2
	
	legs[0].a.setAngle(fl_angle_a)
	#legs[1].a.setAngle(fr_angle_a)
	#legs[2].a.setAngle(bl_angle_a)
	#legs[3].a.setAngle(br_angle_a)
	
	if fl_angle_b >= mid:
		legs[0].b.setAngle(fl_angle_b)

servo.close()
