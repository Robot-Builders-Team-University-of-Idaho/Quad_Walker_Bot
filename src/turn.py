from robot_parts.legs import *
from datetime import datetime
import time

a_low = 150
a_high = 210
b_low = 110
b_high = 190
b_mid = (b_high + b_low) / 2

servo.connect()

# initialize legs and servos
leg_count = 4
legs = []
for i in range(leg_count):
	n = i * 2 + i + 1
	legs.append(leg(n, n+1, n+2))

for i in range(leg_count):
	legs[i].a.setAngle(180)
	legs[i].b.setAngle(180)
	legs[i].c.setAngle(180)

time.sleep(0.75)

for i in range(leg_count):
	legs[i].b.torqueOff()

for i in range(leg_count):
	legs[i].c.setAngle(90)

time.sleep(0.75)

for i in range(leg_count):
	legs[i].b.torqueOn()

legs[0].a.setAngle(a_low)
legs[0].b.setAngle(b_mid)
legs[0].c.setAngle(110)

legs[1].a.setAngle(a_high)
legs[1].b.setAngle(b_mid)
legs[1].c.setAngle(110)

legs[2].a.setAngle(a_high)
legs[2].b.setAngle(b_mid)
legs[2].c.setAngle(110)

legs[3].a.setAngle(a_low)
legs[3].b.setAngle(b_mid)
legs[3].c.setAngle(110)

time.sleep(2)

start = datetime.now()
now = 0
speed = 25

while now < 8_000_000:
	now = datetime.now() - start
	now = (now.seconds * 1_000_000) + now.microseconds
	legs[0].walk(True, now, speed=speed)
	legs[1].walk(False, now, speed=speed)
	legs[2].walk(False, now, speed=speed)
	legs[3].walk(True, now, speed=speed)

for i in range(leg_count):
	legs[i].a.torqueOff()
	legs[i].b.torqueOff()
	legs[i].c.torqueOff()

servo.close()
