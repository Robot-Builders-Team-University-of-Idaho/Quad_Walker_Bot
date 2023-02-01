from robot_parts.servos import *

if not initServos():
	quit()

for i in range(1, 13):
	disableTorque(i)

closeServos()