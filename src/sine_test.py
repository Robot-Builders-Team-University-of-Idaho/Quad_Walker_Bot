from robot_parts.legs import *
from datetime import datetime
import math as m

servo.connect()

fr = leg(1, 2, 3)

#fr.a.setAngle(200)
#fr.b.setAngle(200)
#fr.c.setAngle(200)

ti = datetime.now()
tact = 0

a = 45
z = 0
p = 0.00025

while True:
	t = datetime.now() - ti
	tact = t.microseconds + (t.seconds * 1000000)
	angle = m.degrees(m.radians(a) * m.sin(m.radians((p * tact) + z)) + m.radians(a))
	fr.a.setAngle(angle+135)
	
	if (tact >= 4000000):
		break
		
	
	

servo.close()
