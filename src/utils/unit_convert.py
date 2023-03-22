########################################################################################################################
#
#
# University of Idaho Robotics Club, Mobile Robot Team
#
# Library to convert between units
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

min_vel = 1
max_vel = 450
min_rpm = 0.229
max_rpm = 103

# Convert angle to position value that dynamixel servo can read
def angleToPos(angle: float) -> int:
	# throw exception if parameter is outside range
	if angle < min_angle or angle > max_angle:
		raise ValueError(f"Angle must be between {min_angle} and {max_angle}")

	# use cross multiplication to solve for converted value
	pos = int(angle * max_pos / max_angle)
	# round position to min / max in case the conversion makes it step out of range
	if pos < min_pos: pos = min_pos
	if pos > max_pos: pos = max_pos
	return pos

# Convert dynamixel servo position value to angle
def posToAngle(pos: int) -> float:
	# throw exception if parameter is outside range
	if pos < min_pos or pos > max_pos:
		raise ValueError(f"Position must be between {min_pos} and {max_pos}")
	
	# use cross multiplication to solve for converted value
	angle = pos * max_angle / max_pos
	# round position to min / max in case the conversion makes it step out of range
	if angle < min_angle: angle = min_angle
	if angle > max_angle: angle = max_angle
	return angle

# Convert RPM (rotations per minute) to velocity value that dynamixel servo can read
def rpmToVel(rpm: float) -> int:
	# throw exception if parameter is outside range
	if rpm < min_rpm or rpm > max_rpm:
		raise ValueError(f"RPM must be between {min_rpm} and {max_rpm}")
	
	# use cross multiplication to solve for converted value
	vel = int(rpm * max_vel / max_rpm)
	# round position to min / max in case the conversion makes it step out of range
	if vel < min_vel: vel = min_vel
	if vel > max_vel: vel = max_vel
	return vel

# Convert dynamixel servo velocity value to RPM (rotations per minute)
def velToRPM(vel: int) -> float:
	# throw exception if parameter is outside range
	if vel < min_vel or vel > max_vel:
		raise ValueError(f"Velocity must be between {min_vel} and {max_vel}")

	# use cross multiplication to solve for converted value
	rpm = vel * max_rpm / max_vel
	# round position to min / max in case the conversion makes it step out of range
	if rpm < min_rpm: rpm = min_rpm
	if rpm > max_rpm: rpm = max_rpm
	return rpm
