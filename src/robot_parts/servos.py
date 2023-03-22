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
from utils.unit_convert import *
# Used in wait for angle
import time

# These values are for X Series servos (X330 (5.0 V recommended), X430, X540, 2X430)
# Make sure these values are correct according to the emanual for the device you're using
# DON'T CHANGE THESE VALUES UNLESS YOU KNOW WHAT YOU'RE DOING

# Address for enabling / disabling torque on a servo
addr_torque = 64
# Address for setting a new goal position, causing the servo to rotate
addr_goal_pos = 116
# Address of a servo's current position
addr_curr_pos = 132
# Address for setting a new max velocity that the servo can rotate at while changing position (0 by default, which means inifinte speed)
addr_pro_vel = 112
# Address of a servo's current velocity
addr_curr_vel = 128
# Bits per second that gets transmitted across the servo connection
baudrate = 57600 # TODO: see if this value can be changed to something between 9,600 and 4,500,000 (higher is better)

# Use the actual port assigned to the U2D2.
# ex) Windows: "COM*", Linux: "/dev/ttyUSB*", Mac: "/dev/tty.usbserial-*"
# Use "cat /dev/ttyUSB*" command on raspberry pi CLI to see which usb ports the servos might be connected to
device_path = '/dev/ttyUSB0'
# initialize PortHandler object to read and write through physical (USB) port
port_num = PortHandler(device_path)

# Dynamixel Protocol Version 2.0
# more info:
# https://emanual.robotis.com/docs/en/dxl/protocol2/
protocol_version = 2.0
# Initialize PacketHandler object to use read and write values to servos
packet_handler = PacketHandler(protocol_version)

class servo:
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
		if not port_num.openPort():
			return False

		# Set port baudrate
		if port_num.setBaudRate(baudrate):
			return True
		else:
			return False
	
	# Closes the port to the servos
	# Use this when you're done with the servos / at the end of your program
	def closeServos():
		port_num.closePort()
	
	
	# Constructor for servo object
	# id = id number of the servo
	# torqueOn = whether or not the torque is enabled or disabled when the servo is constructed
	def __init__(self, id: int, torqueOn: bool = True):
		self.id = id
		if torqueOn:
			self.enableTorque()
	
	def __str__(self):
		return str(self.id)

	########################################################################################################################
	#
	#
	# Servo Torque
	#
	#
	########################################################################################################################

	# Enable torque on a servo
	# Returns true if it successfully wrote to the servo, false if it didn't
	def enableTorque(self) -> bool:
		result, error = packet_handler.write1ByteTxRx(port_num, self.id, addr_torque, 1)
		if result != COMM_SUCCESS:
			print("%s" % packet_handler.getTxRxResult(result))
			return False
		elif error != 0:
			print("%s" % packet_handler.getRxPacketError(error))
			return False

		return True

	# Disable torque on a servo
	# Returns true if it successfully wrote to the servo, false if it didn't
	def disableTorque(self) -> bool:
		result, error = packet_handler.write1ByteTxRx(port_num, self.id, addr_torque, 0)
		if result != COMM_SUCCESS:
			print("%s" % packet_handler.getTxRxResult(result))
			return False
		elif error != 0:
			print("%s" % packet_handler.getRxPacketError(error))
			return False

		return True

	# Returns true if the servo's torque is enabled, false if it isn't or if there was an error
	def torqueOn(self) -> bool:
		value, result, error = packet_handler.read1ByteTxRx(port_num, self.id, addr_torque)
		if result != COMM_SUCCESS:
			print("%s" % packet_handler.getTxRxResult(result))
			return False
		elif error != 0:
			print("%s" % packet_handler.getRxPacketError(error))
			return False
		
		return bool(value)

	########################################################################################################################
	#
	#
	# Servo Rotation
	#
	# Note: Angles and Positions (pos) are basically the same thing, except angles are floats that range from 0 to 359, and
	# positions are ints that range from 0 to 4095. The servos only take positions as inputs when being written to, but
	# angles are more intuitive to use so there are setters and getters for both.
	#
	#
	########################################################################################################################

	# Set angle of a servo
	# Returns true if it successfully wrote to the servo, false if it didn't
	def setAngle(self, angle: float) -> bool:
		result, error = packet_handler.write4ByteTxRx(port_num, self.id, addr_goal_pos, angleToPos(angle))
		if result != COMM_SUCCESS:
			print("%s" % packet_handler.getTxRxResult(result))
			return False
		elif error != 0:
			print("%s" % packet_handler.getRxPacketError(error))
			return False
		
		return True

	# Set the position of a servo
	# Returns true if it successfully wrote to the servo, false if it didn't
	def setPos(self, pos: int) -> bool:
		result, error = packet_handler.write4ByteTxRx(port_num, self.id, addr_goal_pos, pos)
		if result != COMM_SUCCESS:
			print("%s" % packet_handler.getTxRxResult(result))
			return False
		elif error != 0:
			print("%s" % packet_handler.getRxPacketError(error))
			return False
		
		return True

	# Reads and returns the current angle of a servo
	# Returns false if the servo wasn't read from successfully
	def getAngle(self):
		current_position, result, error = packet_handler.read4ByteTxRx(port_num, self.id, addr_curr_pos)
		if result != COMM_SUCCESS:
			print("%s" % packet_handler.getTxRxResult(result))
			return False
		elif error != 0:
			print("%s" % packet_handler.getRxPacketError(error))
			return False

		return posToAngle(current_position)

	# Reads and returns the current position of a servo
	# returns false if the servo wasn't read from successfully
	def getPos(self):
		current_position, result, error = packet_handler.read4ByteTxRx(port_num, self.id, addr_curr_pos)
		if result != COMM_SUCCESS:
			print("%s" % packet_handler.getTxRxResult(result))
			return False
		elif error != 0:
			print("%s" % packet_handler.getRxPacketError(error))
			return False

		return current_position

	# Waits for a servo to get to a certain angle
	def waitForAngle(self, angle: float, error: float = 100):
		curr_pos = getPos(self.id)
		time_res = 0.000001
		pos = angleToPos(angle)
		if curr_pos < pos:
			while getPos(self.id) < pos - error:
				time.sleep(time_res)
		elif curr_pos > pos:
			while getPos(self.id) > pos + error:
				time.sleep(time_res)


	########################################################################################################################
	#
	#
	# Velocity Control
	#
	# Note: Veclocity values are measured on the servos in united of 0.229 revolutions / minute and range from 0 to 32,767.
	# 		Default velocity value is 0, which means inifite velocity. Max for 103 rpm is 450 velocity units.
	#
	#
	########################################################################################################################

	# Sets the velocity of a servo
	def setVel(self, vel: int) -> bool:
		result, error = packet_handler.write4ByteTxRx(port_num, self.id, addr_pro_vel, vel)
		if result != COMM_SUCCESS:
			print("%s" % packet_handler.getTxRxResult(result))
			return False
		elif error != 0:
			print("%s" % packet_handler.getRxPacketError(error))
			return False
		
		return True
