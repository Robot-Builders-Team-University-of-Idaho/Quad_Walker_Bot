from robot_parts.legs import *
import time
import os

servo.connect()

# initialize legs and servos
leg_count = 4
legs = []
for i in range(leg_count):
	n = i * 2 + i + 1
	legs.append(leg(n, n+1, n+2))
	legs[i].a.torqueOff()
	legs[i].b.torqueOff()
	legs[i].c.torqueOff()

try:
	while True:
		os.system("clear")
		for i in range(leg_count):
			print(f"({legs[i].a.getAngle()}, {legs[i].b.getAngle()}, {legs[i].c.getAngle()})")
		time.sleep(0.5)
except KeyboardInterrupt:
	print("Ctrl + C pressed...")

servo.close()
