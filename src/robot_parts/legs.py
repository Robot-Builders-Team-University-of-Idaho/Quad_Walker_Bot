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
	# a_start_low = whether the a joint on this leg should start at the low angle or the high angle
	# b_increasing = whether the b joint begins the motion increasing its angle or not
	# t = the time (usually in microseconds) in the sine wave motion to move to
	# speed = a percentage of how fast the leg is moving in the sine wave motion
	# a_low = lowest angle that the a joint can move to in the motion
	# a_high = the highest angle that the a joint can move to in the motion
	# b_low = lowest angle that the b joint can move to in the motion
	# b_high = the highest angle that the b joint can move to in the motion
	def walk(self, a_start_low: bool, b_increasing: bool, t: float, speed: float = 100, a_low: float = 150, a_high: float = 210, b_low: float = 130, b_high: float = 210):
		# Parameter validation

		# Make sure a_start_low is valid
		if type(a_start_low) is not bool:
			raise TypeError("a_start_low parameter must be a bool.")
		
		# Make sure b_increasing is valid
		if type(b_increasing) is not bool:
			raise TypeError("b_increasing parameter must be a bool.")
		
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
		
		# Make sure b_low is valid
		if type(b_low) is not float and type(b_low) is not int:
			raise TypeError(f"b_low parameter must be a float or int between {min_angle} and {max_angle}.")
		if b_low < min_angle or b_low > max_angle:
			raise ValueError(f"b_low parameter must be a float or int between {min_angle} and {max_angle}.")
		# Make sure b_high is valid
		if type(b_high) is not float and type(b_high) is not int:
			raise TypeError(f"b_high parameter must be a float or int between {min_angle} and {max_angle}.")
		if b_high < min_angle or b_high > max_angle:
			raise ValueError(f"b_high parameter must be a float or int between {min_angle} and {max_angle}.")
		
		b_mid = (b_high + b_low) / 2
		
		if a_start_low:
			a_start = a_low
		else:
			a_start = a_high
		
		a_angle = getSineAngle(t, a_low, a_high, a_start, True, speed)
		b_angle = getSineAngle(t, b_low, b_high, b_mid, b_increasing, speed)
		self.a.setAngle(a_angle)
		if b_angle >= b_mid:
			self.b.setAngle(b_angle)
