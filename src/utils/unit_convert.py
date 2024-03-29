########################################################################################################################
#
#
# University of Idaho Robotics Club, Mobile Robot Team
#
# Module to convert between units
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

min_rpm = 0.229
max_rpm = 103
min_vel = 1
max_vel = 450

min_rpm2 = 214.577
max_rpm2 = 7_031_044.56
min_accel = 1
max_accel = 32_767

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

# Convert RPM^2 (rotations per minute squared) to Dynamixel acceleration value
def rpm2ToAccel(rpm2: float) -> int:
	# throw exception if parameter is outside range
	if rpm2 < min_rpm2 or rpm2 > max_rpm2:
		raise ValueError(f"RPM^2 must be between {min_rpm2} and {min_rpm2}")

	# use cross multiplication to solve for converted value
	accel = rpm2 * max_accel / max_rpm2
	# round position to min / max in case the conversion makes it step out of range
	if accel < min_accel: accel = min_accel
	if accel > max_accel: accel = max_accel
	return accel

# Convert dynamixel servo acceleration value to RPM^2 (rotations per minute squared)
def accelToRPM2(accel: int) -> float:
	# throw exception if parameter is outside range
	if accel < min_accel or accel > max_accel:
		raise ValueError(f"Acceleration must be between {min_accel} and {min_accel}")

	# use cross multiplication to solve for converted value
	rpm2 = accel * max_rpm2 / max_accel
	# round position to min / max in case the conversion makes it step out of range
	if rpm2 < min_rpm2: rpm2 = min_rpm2
	if rpm2 > max_rpm2: rpm2 = max_rpm2
	return rpm2
