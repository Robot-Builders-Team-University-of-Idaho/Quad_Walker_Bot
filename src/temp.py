from robot_parts.servos import *

#Enables torque for motors 4,5 and 6
def torqueOn():
    
    enableTorque(4)
    enableTorque(5)
    enableTorque(6)
    
#Disables torque for 4,5 and 6
def torqueOff():
    
    disableTorque(4)
    disableTorque(5)
    disableTorque(6)
    
    #Gets the angle for the servos then sets it to the correct angle
def goAngle():
    getAngle(4)
    if getAngle(4) != 90: setAngle(4, 90)
        
    getAngle(5)
    if getAngle(5) != 90: setAngle(5, 90)
    
    getAngle(6)
    if getAngle(6) != 90: setAngle(6, 90)
    
    

#initialize servo control
if not initServos():
    quit()
    
torqueOn()
    
goAngle()

torqueOff()

    
    
    
    
closeServos()