########################################################################################################################
#
#
# University of Idaho Robotics Club, Mobile Robot Team
#
# Library to control Dynamixel servos for the Quad Leg Walker Robot
#
# Authors / Contributors:
# Chandler Calkins (Fall 2022 - Spring 2023)
#
#
########################################################################################################################

# Dynamixel SDK library
from dynamixel_sdk import *
# Angle to position and position to angle conversion functions
import angle_convert

# These values are for X Series servos (X330 (5.0 V recommended), X430, X540, 2X430)
# Make sure these values are correct according to the emanual for the device you're using
# Don't change these unless you know what you're doing

# Address for enabling / disabling torque on a servo
addr_torque = 64
# Address for setting a new goal position, causing the servo to rotate
addr_goal_pos = 116
# Address of a servo's current position
addr_curr_pos = 132
# Min and Max position values (not used here, just for reference)
min_pos = 0
max_pos = 4095
# Bits per second that gets transmitted across the servo connection
baudrate = 57600 # TODO: see if this value can be changed to something between 9,600 and 4,500,000 (higher is better)

# Use the actual port assigned to the U2D2.
# ex) Windows: "COM*", Linux: "/dev/ttyUSB*", Mac: "/dev/tty.usbserial-*"
# Use "cat /dev/ttyUSB*" command on raspberry pi CLI to see which usb ports the servos might be connected to
device_path = '/dev/ttyUSB0'
# initialize PortHandler object to read and write through physical (USB) port
portHandler = PortHandler(device_path)

# Dynamixel Protocol Version 2.0
# more info:
# https://emanual.robotis.com/docs/en/dxl/protocol2/
protocol_version = 2.0
# initialize PacketHandler object to use read and write functions to servos
packetHandler = PacketHandler(protocol_version)

########################################################################################################################
#
#
# Servo Initialization and Closing
#
#
########################################################################################################################

# Open the port and set the BaudRate for the servos
# Returns false if either of those steps fail, returns true if they both succeed
# Use this at the start of your program to be able to use the servos
def initServos() -> bool:
	# Open port
	if not portHandler.openPort():
		return False

	# Set port baudrate
	if portHandler.setBaudRate(baudrate):
		return True
	else:
		return False

# Closes the port to the servos
# Use this when you're done with the servos / at the end of your program
def closeServos():
	portHandler.closePort()

########################################################################################################################
#
#
# Servo Torque I/O
#
#
########################################################################################################################

# Enable torque on a servo
# Returns true if it successfully wrote to the servo, false if it didn't
def enableTorque(id: int) -> bool:
	result, error = packetHandler.write1ByteTxRx(portHandler, id, addr_torque, 1)
	if result != COMM_SUCCESS:
		print("%s" % packetHandler.getTxRxResult(result))
		return False
	elif error != 0:
		print("%s" % packetHandler.getRxPacketError(error))
		return False

	return True

# Disable torque on a servo
# Returns true if it successfully wrote to the servo, false if it didn't
def disableTorque(id: int) -> bool:
	result, error = packetHandler.write1ByteTxRx(portHandler, id, addr_torque, 0)
	if result != COMM_SUCCESS:
		print("%s" % packetHandler.getTxRxResult(result))
		return False
	elif error != 0:
		print("%s" % packetHandler.getRxPacketError(error))
		return False

	return True

# Returns true if the servo's torque is enabled, false if it isn't or if there was an error
def torqueOn(id: int) -> bool:
	value, result, error = packetHandler.read1ByteTxRx(portHandler, id, addr_torque)
	if result != COMM_SUCCESS:
		print("%s" % packetHandler.getTxRxResult(result))
		return False
	elif error != 0:
		print("%s" % packetHandler.getRxPacketError(error))
		return False
	
	return bool(value)

########################################################################################################################
#
#
# Servo Angle I/O
#
#
########################################################################################################################

# Set angle of a servo
# Returns true if it successfully wrote to the servo, false if it didn't
def setAngle(id: int, angle: float) -> bool:
	result, error = packetHandler.write4ByteTxRx(portHandler, id, addr_goal_pos, angle_convert.angleToPos(angle))
	if result != COMM_SUCCESS:
		print("%s" % packetHandler.getTxRxResult(result))
		return False
	elif error != 0:
		print("%s" % packetHandler.getRxPacketError(error))
		return False
	
	return True

# Reads and returns the current angle of a servo
def getAngle(id: int):
		current_position, result, error = packetHandler.read4ByteTxRx(portHandler, id, addr_curr_pos)
		if result != COMM_SUCCESS:
			print("%s" % packetHandler.getTxRxResult(result))
			return False
		elif error != 0:
			print("%s" % packetHandler.getRxPacketError(error))
			return False

		return angle_convert.posToAngle(current_position)
