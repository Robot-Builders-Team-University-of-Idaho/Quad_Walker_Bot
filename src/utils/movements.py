########################################################################################################################
#
#
# University of Idaho Robotics Club, Mobile Robot Team
#
# Module with functions to make it easier for Jobo to do certain motions
#
# Authors / Contributors:
# Chandler Calkins (Fall 2022 - Spring 2023)
#
#
########################################################################################################################

from utils.unit_convert import *
import math

# Returns the angle of a servo doing a sine wave motion at a given time t
# getSineAngle() = (upper_ang - lower_ang) / 2 * cos((speed * wave_len) * t + start_offset) + ((upper_ang + lower_ang) / 2)
# t = current time in the sine wave motion, aka where on the x axis you are in the sine wave
# lower_ang = the lowest angle in the sine wave motion
# upper_ang = the highest angle in the sine wave motion
# start_ang = the angle that the servo starts the motion at / the horizontal shift of the sine wave / the y-intercept of the sine wave
# forward = whether or not the angle begins increasing or decreasing at the start (True means start increasing (shift sine wave right), False means start decreasing(shift sine wave left))
# speed = a percentage of how fast the servo is moving in the sine wave motion / the percentage of the wave_len
# wave_len = a constant to control what a good max speed of the sine wave motion should be (default is 0.000013)
def getSineAngle(t: float, lower_ang: float, upper_ang: float, start_ang: float, forward: bool, speed: float = 100, wave_len: float = 0.000013) -> float:
	# Make sure t is valid
	if type(t) is not float and type(t) is not int:
		raise TypeError("t parameter must be float or int.")
	
	# Make sure lower_ang is valid
	if type(lower_ang) is not float and type(lower_ang) is not int:
		raise TypeError(f"lower_ang parameter must be float (or int) between {min_angle} and {max_angle}.")
	if lower_ang < min_angle and lower_ang > max_angle:
		raise ValueError(f"lower_ang parameter must be float (or int) between {min_angle} and {max_angle}.")
	
	# Make sure upper_ang is valid
	if type(upper_ang) is not float and type(upper_ang) is not int:
		raise TypeError(f"upper_ang parameter must be float (or int) between {min_angle} and {max_angle}.")
	if upper_ang < min_angle and upper_ang > max_angle:
		raise ValueError(f"upper_ang parameter must be float (or int) between {min_angle} and {max_angle}.")
	
	# Make sure upper_ang is greater than lower_ang
	if upper_ang <= lower_ang:
		raise ValueError(f"upper_ang parameter must be greater than lower_ang parameter.")
	
	# Make sure start_ang is valid
	if type(start_ang) is not float and type(start_ang) is not int:
		raise TypeError(f"start_ang parameter must be float (or int) between lower_ang parameter and upper_ang parameters.")
	if start_ang < lower_ang and start_ang > upper_ang:
		raise ValueError(f"start_ang parameter must be float (or int) between lower_ang parameter and upper_ang parameters.")
	
	# Make sure forward is valid
	if type(forward) is not bool:
		raise TypeError(f"foward parameter must be a bool.")
	
	# Make sure speed is valid
	if type(speed) is not float and type(speed) is not int:
		raise TypeError(f"speed parameter must be a float (or int) greater than 0 on a percentage scale (0 to 100, but you can go above 100).")
	if speed <= 0:
		raise ValueError(f"speed parameter must be a float (or int) greater than 0 on a percentage scale (0 to 100, but you can go above 100).")
	
	# Make sure wave_len is valid
	if type(wave_len) is not float and type(wave_len) is not int:
		raise TypeError(f"wave_len parameter must be float or int.")
	
	# Do the sine wave math
	range = upper_ang - lower_ang
	amplitude = range / 2
	wave_len *= speed / 100
	center = (upper_ang + lower_ang) / 2
	offset = (start_ang - center) * math.pi / range
	# If the wave should be increasing at the start
	if forward:
		offset -= math.pi / 2
	# If the wave should be decreasing at the start
	else:
		offset += math.pi / 2
	return amplitude * math.cos(wave_len * t + offset) + center

# Returns the servo position value of a servo doing a sine wave motion at a given time t
# getSinePos() = (upper_pos - lower_pos) / 2 * cos((speed * wave_len) * t + start_offset) + ((upper_pos + lower_pos) / 2)
# t = current time in the sine wave motion, aka where on the x axis you are in the sine wave
# lower_pos = the lowest servo position in the sine wave motion
# upper_pos = the highest servo position in the sine wave motion
# start_pos = the servo position that the servo starts the motion at / the horizontal shift of the sine wave / the y-intercept of the sine wave
# forward = whether or not the position begins increasing or decreasing at the start (True means start increasing (shift sine wave right), False means start decreasing(shift sine wave left))
# speed = a percentage of how fast the servo is moving in the sine wave motion / the percentage of the wave_len
# wave_len = a constant to control what a good max speed of the sine wave motion should be (default is 0.000013)
def getSinePos(t: float, lower_pos: int, upper_pos: int, start_pos: int, forward: bool, speed: float = 100, wave_len: float = 0.000013) -> int:
	# Make sure t is valid
	if type(t) is not float and type(t) is not int:
		raise TypeError("t parameter must be float or int.")
	
	# Make sure lower_pos is valid
	if type(lower_pos) is not int:
		raise TypeError(f"lower_pos parameter must be int between {min_pos} and {max_pos}.")
	if lower_pos < min_pos and lower_pos > max_pos:
		raise ValueError(f"lower_pos parameter must be int between {min_pos} and {max_pos}.")
	
	# Make sure upper_pos is valid
	if type(upper_pos) is not int:
		raise TypeError(f"upper_pos parameter must be int between {min_pos} and {max_pos}.")
	if upper_pos < min_pos and upper_pos > max_pos:
		raise ValueError(f"upper_pos parameter must be int between {min_pos} and {max_pos}.")
	
	# Make sure upper_pos is greater than lower_pos
	if upper_pos <= lower_pos:
		raise ValueError(f"upper_pos parameter must be greater than lower_pos parameter.")
	
	# Make sure the start_pos is valid
	if type(start_pos) is not int:
		raise TypeError(f"start_pos parameter must be int between lower_pos parameter and upper_pos parameters.")
	if start_pos < lower_pos and start_pos > upper_pos:
		raise ValueError(f"start_pos parameter must be int between lower_pos parameter and upper_pos parameters.")
	
	# Make sure forward is valid
	if type(forward) is not bool:
		raise TypeError(f"foward parameter must be a bool.")
	
	# Make sure speed is valid
	if type(speed) is not float and type(speed) is not int:
		raise TypeError(f"speed parameter must be a int greater than 0 on a percentage scale (0 to 100, but you can go above 100).")
	if speed <= 0:
		raise ValueError(f"speed parameter must be a int greater than 0 on a percentage scale (0 to 100, but you can go above 100).")
	
	# Make sure wave_len is valid
	if type(wave_len) is not float and type(wave_len) is not int:
		raise TypeError(f"wave_len parameter must be float or int.")
	
	# Do the sine wave math
	range = upper_pos - lower_pos
	amplitude = range / 2
	wave_len *= speed / 100
	center = (upper_pos + lower_pos) / 2
	offset = (start_pos - center) * math.pi / range
	# If the wave should be increasing at the start
	if forward:
		offset -= math.pi / 2
	# If the wave should be decreasing at the start
	else:
		offset += math.pi / 2
	return round(amplitude * math.cos(wave_len * t + offset) + center)
