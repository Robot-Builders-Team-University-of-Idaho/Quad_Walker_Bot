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