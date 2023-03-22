from robot_parts.servos import *
import time

servo.initServos()

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

servo.closeServos()
