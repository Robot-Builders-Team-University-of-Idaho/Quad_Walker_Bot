########################################################################################################################
#
#
# University of Idaho Robotics Club, Mobile Robot Team
#
# Module to control Dynamixel XL330-M288-T servos for the Quad Leg Walker Robot
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
# Address for setting a new max velocity that the servo can rotate at while changing position
# (0 by default, which means inifinte / max speed)
addr_pro_vel = 112
# Address of a servo's current velocity
addr_curr_vel = 128
# Address for setting a servo's acceleration to get up to max speed and get down to a stop when changing position
addr_pro_acl = 108
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

# list to keep track of servos that are currently in use
active_servos = []

class servo:
	########################################################################################################################
	#
	#
	# Servo Initialization and Closing
	#
	#
	########################################################################################################################

	# Open the connection / port and set the BaudRate for the servos
	# Returns false if either of those steps fail, returns true if they both succeed
	# Use this at the start of your program to be able to use the servos
	def connect() -> bool:
		# Open port
		if not port_num.openPort():
			return False

		# Set port baudrate
		if port_num.setBaudRate(baudrate):
			return True
		else:
			return False
	
	# Closes the connection / port to the servos
	# Use this when you're done with the servos / at the end of your program
	def close():
		# disable torque on all active servos and remove them from list
		#for s in active_servos:
		#	s.torqueOff()
		#	active_servos.remove(s)
		
		port_num.closePort()
	
	# Constructor
	# id = id number of the servo
	# torqueOn = whether or not the torque is enabled or disabled when the servo is constructed
	def __init__(self, id: int, torque_on: bool = True):
		# if id isn't an int
		if type(id) is not int:
			raise TypeError("id parameter for servo constructor must be int between 1 and 253.")
		# if torque_on isn't a bool
		if type(torque_on) is not bool:
			raise TypeError("torque_on parameter for servo constructor must be bool.")
		# if id is out of range (1 - 253)
		if id < 1 or id > 253:
			raise ValueError("id parameter for servo constructor must be int between 1 and 253.")

		self.id = id
		# adds servo object to list of servos that are currently in use
		active_servos.append(self)
		if torque_on:
			self.torqueOn()
	
	# Destructor
	#def __del__(self):
	#	if self in active_servos:
	#		self.torqueOff()
	#		active_servos.remove(self)

	########################################################################################################################
	#
	#
	# Utility Functions
	#
	#
	########################################################################################################################

	# String casting function
	def __str__(self):
		return f"Servo({self.id})"
	
	# Checks for communication errors
	# Returns true if there were no errors, false if there was an error
	def __commErrorCheck(self, result, error, func_name: str) -> bool:
		# make sure func_name is a string
		if type(func_name) is not str:
			raise TypeError("func_name parameter for __commErrorCheck must be a string of the name of the function you're checking for a communication error in.")
		
		# check for errors returned from trying to communicate with the servo
		if result != COMM_SUCCESS:
			# used to be "print("%s" % packet_handler.getTxRxResult(result))"
			print(f"Servo {self.id} ({func_name}): {packet_handler.getTxRxResult(result)}")
			return False
		elif error != 0:
			print(f"Servo {self.id} ({func_name}): {packet_handler.getRxPacketError(error)}")
			return False
		
		return True

	########################################################################################################################
	#
	#
	# Servo Torque
	#
	#
	########################################################################################################################

	# Turns on the torque of a servo
	# Returns true if it successfully wrote to the servo, false if it didn't
	def torqueOn(self) -> bool:
		# send value of 1 to torque address
		result, error = packet_handler.write1ByteTxRx(port_num, self.id, addr_torque, 1)
		# check for errors returned from servo
		return self.__commErrorCheck(result, error, "torqueOn")

	# Turns off the torque of a servo
	# Returns true if it successfully wrote to the servo, false if it didn't
	def torqueOff(self) -> bool:
		# send value of 0 to torque address
		result, error = packet_handler.write1ByteTxRx(port_num, self.id, addr_torque, 0)
		# check for errors returned from servo
		return self.__commErrorCheck(result, error, "torqueOff")

	# Returns true if the servo's torque is on, false if it isn't or if there was an error
	def torqueIsOn(self) -> bool:
		# request current value at torque address
		value, result, error = packet_handler.read1ByteTxRx(port_num, self.id, addr_torque)
		# check for errors returned from servo
		if not self.__commErrorCheck(result, error, "torqueIsOn"):
			return False
		
		return bool(value)
	
	# Returns true if the servo's torque is off, false if it isn't or if there was an error
	def torqueIsOff(self) -> bool:
		# request current value at torque address
		value, result, error = packet_handler.read1ByteTxRx(port_num, self.id, addr_torque)
		# check for errors returned from servo
		if not self.__commErrorCheck(result, error, "torqueIsOn"):
			return False
		
		return not bool(value)

	########################################################################################################################
	#
	#
	# Servo Position
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
		# make sure angle is right type
		if type(angle) is not float and type(angle) is not int:
			raise TypeError(f"angle parameter must be of type float (or int) between {min_angle} and {max_angle}.")
		# make sure the angle is within range
		if angle < min_angle or angle > max_angle:
			raise ValueError(f"angle parameter must be of type float (or int) between {min_angle} and {max_angle}.")
		
		# convert angle to position value and send it to goal position address
		result, error = packet_handler.write4ByteTxRx(port_num, self.id, addr_goal_pos, angleToPos(angle))
		# check for errors returned from servo
		return self.__commErrorCheck(result, error, "setAngle")

	# Set the position of a servo
	# Returns true if it successfully wrote to the servo, false if it didn't
	def setPos(self, pos: int) -> bool:
		# make sure pos is the right type
		if type(pos) is not int:
			raise TypeError(f"pos parameter must be of type int between {min_pos} and {max_pos}.")
		# make sure the position is within range
		if pos < min_pos or pos > max_pos:
			raise ValueError(f"pos parameter must be of type int between {min_pos} and {max_pos}.")
		
		# send position value to goal position address
		result, error = packet_handler.write4ByteTxRx(port_num, self.id, addr_goal_pos, pos)
		# check for errors returned from servo
		return self.__commErrorCheck(result, error, "setPos")

	# Reads and returns the current angle of a servo
	# Returns false if the servo wasn't read from successfully
	def getAngle(self):
		# request current value at present position address
		current_position, result, error = packet_handler.read4ByteTxRx(port_num, self.id, addr_curr_pos)
		# check for errors returned from servo
		if not self.__commErrorCheck(result, error, "getAngle"):
			return False

		return posToAngle(current_position)

	# Reads and returns the current position of a servo
	# returns false if the servo wasn't read from successfully
	def getPos(self):
		# request current value at present position address
		current_position, result, error = packet_handler.read4ByteTxRx(port_num, self.id, addr_curr_pos)
		# check for errors returned from servo
		if not self.__commErrorCheck(result, error, "getPos"):
			return False

		return current_position

	# Waits for a servo to get to a certain angle
	# angle = angle to wait for servo to reach
	# error = number of position values away from angle to cause the wait to end if the servo comes within that range
	def waitForAngle(self, angle: float, error: float = 100):
		# make sure angle is right type
		if type(angle) is not float and type(angle) is not int:
			raise TypeError(f"angle parameter must be of type float (or int) between {min_angle} and {max_angle}.")
		# make sure the angle is within range
		if angle < min_angle or angle > max_angle:
			raise ValueError(f"angle parameter must be of type float (or int) between {min_angle} and {max_angle}.")
		
		# function to get the current position and check for errors
		def currPos() -> int:
			# get the current position
			curr_pos = self.getPos()
			# check for communication errors
			if type(curr_pos) is bool and curr_pos == False:
				raise IOError(f"Failed to communicate with servo {self.id}.")
			
			return curr_pos
		
		# get the current position
		curr_pos = currPos()
		# check for communication errors
		if type(curr_pos) is bool and curr_pos == False:
			raise IOError(f"Failed to communicate with servo {self.id}.")
		# wait time time resolution
		time_res = 0.000001
		# get the position value of the angle
		pos = angleToPos(angle)
		if curr_pos < pos:
			# get the current position
			curr_pos = currPos()
			while curr_pos < pos - error:
				time.sleep(time_res)
				# get the current position
				curr_pos = currPos()
		elif curr_pos > pos:
			# get the current position
			curr_pos = currPos()
			while curr_pos > pos + error:
				time.sleep(time_res)
				# get the current position
				curr_pos = currPos()
	
	# Waits for a servo to get to a certain position
	# pos = position to wait for servo to reach
	# error = number of position values away from pos to cause the wait to end if the servo comes within that range
	def waitForPos(self, pos: int, error: float = 100):
		# make sure pos is the right type
		if type(pos) is not int:
			raise TypeError(f"pos parameter must be of type int between {min_pos} and {max_pos}.")
		# make sure the position is within range
		if pos < min_pos or pos > max_pos:
			raise ValueError(f"pos parameter must be of type int between {min_pos} and {max_pos}.")
		
		# function to get the current position and check for errors
		def currPos() -> int:
			# get the current position
			curr_pos = self.getPos()
			# check for communication errors
			if type(curr_pos) is bool and curr_pos == False:
				raise IOError(f"Failed to communicate with servo {self.id}.")
			
			return curr_pos
		
		# get the current position
		curr_pos = currPos()
		# wait time time resolution
		time_res = 0.000001
		if curr_pos < pos:
			# get the current position
			curr_pos = currPos()
			while curr_pos < pos - error:
				time.sleep(time_res)
				# get the current position
				curr_pos = currPos()
		elif curr_pos > pos:
			# get the current position
			curr_pos = currPos()
			while curr_pos > pos + error:
				time.sleep(time_res)
				# get the current position
				curr_pos = currPos()

	########################################################################################################################
	#
	#
	# Servo Speed
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
		# make sure rpm is right type
		if type(rpm) is not float and type(rpm) is not int:
			raise TypeError(f"rpm parameter must be of type float (or int) between {min_rpm} and {max_rpm}.")
		# make sure the rpm is within range
		if rpm < min_rpm or rpm > max_rpm:
			raise ValueError(f"rpm parameter must be of type float (or int) between {min_rpm} and {max_rpm}.")
		
		# convert rpm to velocity value and send it to profile velocity address
		result, error = packet_handler.write4ByteTxRx(port_num, self.id, addr_pro_vel, rpmToVel(rpm))
		# check for errors returned from servo
		return self.__commErrorCheck(result, error, "setRPM")

	# Sets the velocity of a servo
	# Returns true if it successfully wrote to the servo, false if it didn't
	def setVel(self, vel: int) -> bool:
		# make sure vel is the right type
		if type(vel) is not int:
			raise TypeError(f"vel parameter must be of type int between {min_vel} and {max_vel}.")
		# make sure the velocity is within range
		if vel < min_vel or vel > max_vel:
			raise ValueError(f"vel parameter must be of type int between {min_vel} and {max_vel}.")
		
		# send velocity value to profile velocity address
		result, error = packet_handler.write4ByteTxRx(port_num, self.id, addr_pro_vel, vel)
		# check for errors returned from servo
		return self.__commErrorCheck(result, error, "setVel")
	
	# Reads the current RPM of the servo
	# Returns false if the servo wasn't read from successfully
	def getRPM(self):
		# request current value at present velocity address
		current_velocity, result, error = packet_handler.read4ByteTxRx(port_num, self.id, addr_curr_vel)
		# check for errors returned from servo
		if not self.__commErrorCheck(result, error, "getRPM"):
			return False

		return rpmToVel(current_velocity)
	
	# Reads the current velocity of the servo
	# Returns false if the servo wasn't read from successfully
	def getRPM(self):
		# request current value at present velocity address
		current_velocity, result, error = packet_handler.read4ByteTxRx(port_num, self.id, addr_curr_vel)
		# check for errors returned from servo
		if not self.__commErrorCheck(result, error, "getVel"):
			return False

		return current_velocity
	
	########################################################################################################################
	#
	#
	# Servo Acceleration
	#
	# Note: RPM^2 (rotations per minute squared) and acceleration values (accel) are basically the same thing, except rpm2s
	# are floats that range from 214.577 to 7,031,044.56, and acceleration values are ints that range from 1 to 32,767. The
	# servos use acceleration values internally, but it can be simpler to use rpm2 sometimes.
	#
	# Note: Acceleration values are measured on the servos in units of 214.577 rpm2 and range from 0 to 32,767. The default
	# acceleration value is 0, which means inifite acceleration and is basically the same as 32,767.
	#
	#
	########################################################################################################################

	# Sets the RPM^2 (rotations per minute squared) of a servo
	# Returns true if it successfully wrote to the servo, false if it didn't
	def setRPM2(self, rpm2: float) -> bool:
		# make sure rpm is right type
		if type(rpm2) is not float and type(rpm2) is not int:
			raise TypeError(f"rpm2 parameter must be of type float (or int) between {min_rpm2} and {max_rpm2}.")
		# make sure the rpm is within range
		if rpm2 < min_rpm2 or rpm2 > max_rpm2:
			raise ValueError(f"rpm2 parameter must be of type float (or int) between {min_rpm2} and {max_rpm2}.")
		
		# convert rpm2 to acceleration value and send it to profile acceleration address
		result, error = packet_handler.write4ByteTxRx(port_num, self.id, addr_pro_vel, rpm2ToAccel(rpm2))
		# check for errors returned from servo
		return self.__commErrorCheck(result, error, "setRPM2")
	
	# Sets the acceleration of a servo
	# Returns true if it successfully wrote to the servo, false if it didn't
	def setAccel(self, accel: int) -> bool:
		# make sure accel is the right type
		if type(accel) is not int:
			raise TypeError(f"accel parameter must be of type int between {min_accel} and {max_accel}.")
		# make sure the velocity is within range
		if accel < min_accel or accel > max_accel:
			raise ValueError(f"accel parameter must be of type int between {min_accel} and {max_accel}.")
		
		# send acceleration value to profile acceleration address
		result, error = packet_handler.write4ByteTxRx(port_num, self.id, addr_pro_acl, accel)
		# check for errors returned from servo
		return self.__commErrorCheck(result, error, "setAccel")
