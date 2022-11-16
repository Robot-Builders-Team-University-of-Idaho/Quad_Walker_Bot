########################################################################################################################
#
#
# University of Idaho Robotics Club, Mobile Robot Team
#
# Library to convert between angles and position values that Dynamixel servos can read
#
# Authors / Contributors:
# Chandler Calkins (Fall 2022 - Spring 2023)
#
#
########################################################################################################################

min_angle = 0
max_angle = 359
min_pos = 0
max_pos = 4095

# Convert angle to position that dynamixel servo can read
# min_angle < angle < max_angle
def angleToPos(angle: float) -> int:
	# throw exception if parameter is outside angle range
    if (angle < min_angle or angle > max_angle):
        raise Exception(f'Angle must be between {min_angle} and {max_angle}')
    
	# use cross multiplication to solve for converted value
    return int(angle * max_pos / max_angle)

# Convert dynamixel servo position to angle
# min_pos < pos < max_pos
def posToAngle(pos: int) -> float:
	# throw exception if parameter is outside position range
    if (pos < min_pos or pos > max_pos):
        raise Exception(f'Position must be between {min_pos} and {max_pos}')
    
	# use cross multiplication to solve for converted value
    return pos * max_angle / max_pos
