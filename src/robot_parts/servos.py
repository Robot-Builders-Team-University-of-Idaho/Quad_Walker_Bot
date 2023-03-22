########################################################################################################################
#
#
# University of Idaho Robotics Club, Mobile Robot Team
#
# Library to control Dynamixel XL330-M288-T servos for the Quad Leg Walker Robot
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
# The servo model that is being used for this project is the XL330-M288-T
# Refer to the control table for this servo to find out more: https://emanual.robotis.com/docs/en/dxl/x/xl330-m288/
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
	
	# Constructor
	# id = id number of the servo
	# torqueOn = whether or not the torque is enabled or disabled when the servo is constructed
	def __init__(self, id: int, torqueOn: bool = True):
		self.id = id
		if torqueOn:
			self.enableTorque()
	
	# String casting function
	def __str__(self):
		return f"Servo {self.id}"
	
	# Destructor
	def __del__(self):
		self.disableTorque()

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
		# send value of 1 to torque address
		result, error = packet_handler.write1ByteTxRx(port_num, self.id, addr_torque, 1)
		# check for errors returned from servo
		if result != COMM_SUCCESS:
			# used to be "print("%s" % packet_handler.getTxRxResult(result))"
			print(f"Servo {self.id} (enableTorque): {packet_handler.getTxRxResult(result)}")
			return False
		elif error != 0:
			print(f"Servo {self.id} (enableTorque): {packet_handler.getRxPacketError(error)}")
			return False

		return True

	# Disable torque on a servo
	# Returns true if it successfully wrote to the servo, false if it didn't
	def disableTorque(self) -> bool:
		# send value of 0 to torque address
		result, error = packet_handler.write1ByteTxRx(port_num, self.id, addr_torque, 0)
		# check for errors returned from servo
		if result != COMM_SUCCESS:
			print(f"Servo {self.id} (disableTorque): {packet_handler.getTxRxResult(result)}")
			return False
		elif error != 0:
			print(f"Servo {self.id} (disableTorque): {packet_handler.getRxPacketError(error)}")
			return False

		return True

	# Returns true if the servo's torque is enabled, false if it isn't or if there was an error
	def torqueOn(self) -> bool:
		# request current value at torque address
		value, result, error = packet_handler.read1ByteTxRx(port_num, self.id, addr_torque)
		# check for errors returned from servo
		if result != COMM_SUCCESS:
			print(f"Servo {self.id} (torqueOn): {packet_handler.getTxRxResult(result)}")
			return False
		elif error != 0:
			print(f"Servo {self.id} (torqueOn): {packet_handler.getRxPacketError(error)}")
			return False
		
		return bool(value)

	########################################################################################################################
	#
	#
	# Servo Rotation
	#
	# Note: Angles and Positions (pos) are basically the same thing, except angles are floats that range from 0 to 359, and
	# positions are ints that range from 0 to 4095. The servos use position values internally, but angles are simpler to use
	# sometimes.
	#
	#
	########################################################################################################################

	# Set angle of a servo
	# Returns true if it successfully wrote to the servo, false if it didn't
	def setAngle(self, angle: float) -> bool:
		# make sure the angle is within range
		if angle < min_angle or angle > max_angle:
			print(f"Servo {self.id} (setAngle): Angle {angle} is out of range ({min_angle} - {max_angle})")
			return False
		# convert angle to position value and send it to goal position address
		result, error = packet_handler.write4ByteTxRx(port_num, self.id, addr_goal_pos, angleToPos(angle))
		# check for errors returned from servo
		if result != COMM_SUCCESS:
			print(f"Servo {self.id} (setAngle): {packet_handler.getTxRxResult(result)}")
			return False
		elif error != 0:
			print(f"Servo {self.id} (setAngle): {packet_handler.getRxPacketError(error)}")
			return False
		
		return True

	# Set the position of a servo
	# Returns true if it successfully wrote to the servo, false if it didn't
	def setPos(self, pos: int) -> bool:
		# make sure the position is within range
		if pos < min_pos or pos > max_pos:
			print(f"Servo {self.id} (setPos): Position {pos} is out of range ({min_pos} - {max_pos})")
			return False
		# send position value to goal position address
		result, error = packet_handler.write4ByteTxRx(port_num, self.id, addr_goal_pos, pos)
		# check for errors returned from servo
		if result != COMM_SUCCESS:
			print(f"Servo {self.id} (setPos): {packet_handler.getTxRxResult(result)}")
			return False
		elif error != 0:
			print(f"Servo {self.id} (setPos): {packet_handler.getRxPacketError(error)}")
			return False
		
		return True

	# Reads and returns the current angle of a servo
	# Returns false if the servo wasn't read from successfully
	def getAngle(self):
		# request current value at current position address
		current_position, result, error = packet_handler.read4ByteTxRx(port_num, self.id, addr_curr_pos)
		# check for errors returned from servo
		if result != COMM_SUCCESS:
			print(f"Servo {self.id} (getAngle): {packet_handler.getTxRxResult(result)}")
			return False
		elif error != 0:
			print(f"Servo {self.id} (getAngle): {packet_handler.getRxPacketError(error)}")
			return False

		return posToAngle(current_position)

	# Reads and returns the current position of a servo
	# returns false if the servo wasn't read from successfully
	def getPos(self):
		# request current value at current position address
		current_position, result, error = packet_handler.read4ByteTxRx(port_num, self.id, addr_curr_pos)
		# check for errors returned from servo
		if result != COMM_SUCCESS:
			print(f"Servo {self.id} (getPos): {packet_handler.getTxRxResult(result)}")
			return False
		elif error != 0:
			print(f"Servo {self.id} (getPos): {packet_handler.getRxPacketError(error)}")
			return False

		return current_position

	# Waits for a servo to get to a certain angle
	# angle = angle to wait for servo to reach
	# error = number of position values away from angle to cause the wait to end if the servo comes within that range
	def waitForAngle(self, angle: float, error: float = 100):
		# make sure the angle is within range
		if angle < min_angle or angle > max_angle:
			print(f"Servo {self.id} (waitForAngle): Angle {angle} is out of range ({min_angle} - {max_angle})")
			return False
		# get the current position
		curr_pos = self.getPos()
		# wait time time resolution
		time_res = 0.000001
		# get the position value of the angle
		pos = angleToPos(angle)
		if curr_pos < pos:
			while self.getPos() < pos - error:
				time.sleep(time_res)
		elif curr_pos > pos:
			while self.getPos() > pos + error:
				time.sleep(time_res)
	
	# Waits for a servo to get to a certain position
	# pos = position to wait for servo to reach
	# error = number of position values away from pos to cause the wait to end if the servo comes within that range
	def waitForPos(self, pos: int, error: float = 100):
		# make sure the position is within range
		if pos < min_pos or pos > max_pos:
			print(f"Servo {self.id} (waitForPos): Position {pos} is out of range ({min_pos} - {max_pos})")
			return False
		# get the current position
		curr_pos = self.getPos()
		# wait time time resolution
		time_res = 0.000001
		if curr_pos < pos:
			while self.getPos() < pos - error:
				time.sleep(time_res)
		elif curr_pos > pos:
			while self.getPos() > pos + error:
				time.sleep(time_res)

	########################################################################################################################
	#
	#
	# Speed Control
	#
	# Note: RPM (rotations per minute) and velocity values (vel) are basically the same thing, except rpms are floats that
	# range from 0.229 to 103, and velocity values are ints that range from 1 to 450. The servos use velocity values
	# internally, but it can be simpler to use rpm sometimes.
	#
	# Note: Veclocity values are measured on the servos in units of 0.229 rpm and range from 0 to 32,767. The default
	# velocity value is 0, which means inifite velocity and is basically the same as 32,767. Max rpm for the XL330-M288-T
	# servo is 103 rpm, which is equal to just under 450 velocity units, so the actual allowed range of velocity units is 1
	# to 450 since the rpm of the XL330-M288-T servo ranges from 0.229 to 103.
	#
	#
	########################################################################################################################

	# Sets the RPM (rotations per minute) of a servo
	# Returns true if it successfully wrote to the servo, false if it didn't
	def setRPM(self, rpm: float) -> bool:
		# make sure the velocity is within range
		if rpm < min_rpm or rpm > max_rpm:
			print(f"Servo {self.id} (setRPM): RPM {rpm} is out of range ({min_rpm} - {max_rpm})")
			return False
		# convert rpm to velocity value and send it to profile velocity address
		result, error = packet_handler.write4ByteTxRx(port_num, self.id, addr_pro_vel, rpmToVel(rpm))
		# check for errors returned from servo
		if result != COMM_SUCCESS:
			print(f"Servo {self.id} (setRPM): {packet_handler.getTxRxResult(result)}")
			return False
		elif error != 0:
			print(f"Servo {self.id} (setRPM): {packet_handler.getRxPacketError(error)}")
			return False
		
		return True

	# Sets the velocity of a servo
	# Returns true if it successfully wrote to the servo, false if it didn't
	def setVel(self, vel: int) -> bool:
		# make sure the velocity is within range
		if vel < min_vel or vel > max_vel:
			print(f"Servo {self.id} (setVel): Velocity {vel} is out of range ({min_vel} - {max_vel})")
			return False
		# send velocity value to profile velocity address
		result, error = packet_handler.write4ByteTxRx(port_num, self.id, addr_pro_vel, vel)
		# check for errors returned from servo
		if result != COMM_SUCCESS:
			print(f"Servo {self.id} (setVel): {packet_handler.getTxRxResult(result)}")
			return False
		elif error != 0:
			print(f"Servo {self.id} (setVel): {packet_handler.getRxPacketError(error)}")
			return False
		
		return True
