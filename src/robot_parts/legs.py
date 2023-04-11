########################################################################################################################
#
#
# University of Idaho Robotics Club, Mobile Robot Team
#
# Module for servo leg class
#
# Authors / Contributors:
# Chandler Calkins (Fall 2022 - Spring 2023)
#
#
########################################################################################################################

from robot_parts.servos import *
from utils.movements import *

# Storage class for holding 3 servos that are all on the same leg
class leg:
	# Constructor for leg class
	# You can give it either ints for servo ids or already constructed servos for each servo field
	def __init__(self, a, b, c, a_torque_on: bool = True, b_torque_on: bool = True, c_torque_on: bool = True):
		# if a is an id, construct new servo
		if type(a) is int:
			self.a = servo(a, torque_on=a_torque_on)
		# if a is an already constructed servo, use that one
		elif type(a) is servo:
			self.a = a
		else:
			raise TypeError("leg constructor can only take either type int or type servo for each joint.")
		
		# if b is an id, construct new servo
		if type(b) is int:
			self.b = servo(b, torque_on=b_torque_on)
		# if b is an already constructed servo, use that one
		elif type(b) is servo:
			self.b = b
		else:
			raise TypeError("leg constructor can only take either type int or type servo for each joint.")
		
		# if c is an id, construct new servo
		if type(c) is int:
			self.c = servo(c, torque_on=c_torque_on)
		# if c is an already constructed servo, use that one
		elif type(c) is servo:
			self.c = c
		else:
			raise TypeError("leg constructor can only take either type int or type servo for each joint.")
	
	# String caster
	def __str__(self):
		return f"Leg({self.a}, {self.b}, {self.b})"
	
	# Makes the leg to a sine wave-like walking motion
	# start_low = whether this leg should start at the low angle or the high angle
	# t = the time (usually in microseconds) in the sine wave motion to move to
	# speed = a percentage of how fast the leg is moving in the sine wave motion
	# a_low = lowest angle that the a joint can move to in the motion
	# a_high = the highest angle that the a joint can move to in the motion
	def walk(self, start_low: bool, t: float, speed: float = 100, a_low: float = 135, a_high: float = 225):
		# Parameter validation

		# Make sure start_low is valid
		if type(start_low) is not bool:
			raise TypeError("start_low parameter must be a bool.")
		
		# Make sure t is valid
		if type(t) is not float and type(t) is not int:
			raise TypeError("t parameter must be a float or int.")
		
		# Make sure speed is valid
		if type(speed) is not float and type(speed) is not int:
			raise TypeError("speed parameter must be a float or int greater than 0.")
		if speed < 0:
			raise ValueError("speed parameter must be a float or int greater than 0.")
		
		# Make sure a_low is valid
		if type(a_low) is not float and type(a_low) is not int:
			raise TypeError(f"a_low parameter must be a float or int between {min_angle} and {max_angle}.")
		if a_low < min_angle or a_low > max_angle:
			raise ValueError(f"a_low parameter must be a float or int between {min_angle} and {max_angle}.")
		
		# Make sure a_high is valid
		if type(a_high) is not float and type(a_high) is not int:
			raise TypeError(f"a_high parameter must be a float or int between {min_angle} and {max_angle}.")
		if a_high < min_angle or a_high > max_angle:
			raise ValueError(f"a_high parameter must be a float or int between {min_angle} and {max_angle}.")
		
		b_low = 150
		b_high = 190

		a_start = a_high
		b_start = b_high
		if start_low:
			a_start = a_low
			b_start = b_low
		
		self.a.setAngle(getSineAngle(t, a_low, a_high, a_start, True, speed))
		self.b.setAngle(getSineAngle(t, b_low, b_high, b_start, True, speed))
