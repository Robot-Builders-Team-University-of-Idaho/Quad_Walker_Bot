from robot_parts.servos import *

# returns true if a string is an integer, false if not
def isInt(input: str) -> bool:
	try:
		int(input)
		return True
	except ValueError:
		return False

# returns true if a string is a float, false if not
def isFloat(input: str) -> bool:
	try:
		float(input)
		return True
	except ValueError:
		return False

# initialize servo control
# if it fails, quit the program
if not servo.connect():
	quit()

# list to store all of the servos whos torque has been turned on so they can be turned off at the end
servos = []

# loop until user inputs something that's not a number (just pressing enter works too)
while True:
	print("Type anything that's not a number to quit")

	# get the id of the servo to rotate
	id = input("Enter a servo ID: ")
	# if the id is not a valid integer, end the program
	if not isInt(id):
		break
	# otherwise, convert the input into an int value
	else:
		id = int(id)
	
	# get the angle to rotate that servo to
	angle = input("Enter an angle between 0 and 359: ")
	# if the angle is not a valid float, end the program
	if not isFloat(angle):
		break
	# otherwise, convert the input into a float value
	else:
		angle = float(angle)
	
	# check to see if servo id has already been used
	index = 0
	for i in range(len(servos)):
		if servos[i].id == id:
			index = i
			break
		else:
			index += 1
	
	# if the servo id hasn't been used, add that servo to the list
	if index >= len(servos):
		servos.append(servo(id))
	
	# try turning the servo to the inputted angle
	servos[index].setAngle(angle)

# loop through each of the servos that had its torque turned on and disable it
for s in servos:
	s.torqueOff()

# close down servo control
servo.close()