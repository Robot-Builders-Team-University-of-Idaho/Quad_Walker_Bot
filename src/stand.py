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

time.sleep(0.5)
#for i in range(leg_count):
	#legs[i].a.waitForAngle(180)
	#legs[i].b.waitForAngle(180)
	#legs[i].c.waitForAngle(180)

# make jobo stand up
for i in range(leg_count):
	legs[i].b.setAngle(200)
	legs[i].c.setAngle(150)

time.sleep(0.5)
#for i in range(leg_count):
	#legs[i].b.waitForAngle(200)
	#legs[i].c.waitForAngle(150)

# make jobo stand up a bit taller
for i in range(leg_count):
	legs[i].b.setAngle(150)

time.sleep(0.5)
#for i in range(leg_count):
	#legs[i].b.waitForAngle(150)

# make jobo twist back and forth a few times
for i in range(5):
	for i in range(leg_count):
		legs[i].a.setAngle(150)
	
	time.sleep(0.5)
	#for i in range(leg_count):
		#legs[i].a.waitForAngle(150)
	
	for i in range(leg_count):
		legs[i].a.setAngle(210)
	
	time.sleep(0.5)
	#for i in range(leg_count):
		#legs[i].a.waitForAngle(210)

legs = 4 # of legs on jobo
joints = 3 # number of joints per leg

i = 1
# matrix of servos (2D list)
# row 0 is front left (fl), 1 is front right (fr), 2 is back left (bl), 3 is back right (br)
# col 0 is the servo closest to the center, 1 is the middle servo, and 2 is the last servo
servos = []
# initialize all of the servos
for row in range(legs):
	servos.append([])
	for col in range(joints):
		servos[row].append(servo(i))
		i += 1

# set all of the servos to a straight angle
for row in range(legs):
	for col in range(joints):
		servos[row][col].setAngle(180)

time.sleep(0.75)

# make jobo stand up
for row in range(legs):
	servos[row][1].setAngle(200)
	servos[row][2].setAngle(150)

time.sleep(0.75)

# make jobo stand up taller
for row in range(legs):
	servos[row][1].setAngle(150)

time.sleep(0.75)

# make jobo twist back and forth a few times
for i in range(5):
	for row in range(legs):
		servos[row][0].setAngle(150)
	
	time.sleep(0.5)

	for row in range(legs):
		servos[row][0].setAngle(210)
	
	time.sleep(0.5)

time.sleep(0.25)

fl = []
fr = []
bl = []
br = []

fl.append(servo(1))
fl.append(servo(2))
fl.append(servo(3))

fr.append(servo(4))
fr.append(servo(5))
fr.append(servo(6))

bl.append(servo(7))
bl.append(servo(8))
bl.append(servo(9))

br.append(servo(10))
br.append(servo(11))
br.append(servo(12))

fl[0].setAngle(180)
fr[0].setAngle(180)
bl[0].setAngle(180)
br[0].setAngle(180)

fl[1].setAngle(180)
fr[1].setAngle(180)
bl[1].setAngle(180)
br[1].setAngle(180)

fl[2].setAngle(180)
fr[2].setAngle(180)
bl[2].setAngle(180)
br[2].setAngle(180)

time.sleep(0.75)

fl[1].setAngle(200)
fr[1].setAngle(200)
bl[1].setAngle(200)
br[1].setAngle(200)

fl[2].setAngle(150)
fr[2].setAngle(150)
bl[2].setAngle(150)
br[2].setAngle(150)

time.sleep(0.75)

fl[1].setAngle(150)
fr[1].setAngle(150)
bl[1].setAngle(150)
br[1].setAngle(150)

time.sleep(0.75)

fl[0].setAngle(150)
fr[0].setAngle(150)
bl[0].setAngle(150)
br[0].setAngle(150)

servo.close()
