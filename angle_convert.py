min_angle = 0
max_angle = 360
min_pos = 0
max_pos = 4096

# convert angle to position that dynamixel servo can read
# (angle between 0 and 360)
def angle_to_pos(angle: float):
    if (angle < min_angle or angle > max_angle):
        raise Exception(f'Angle must be between 0 and {max_angle}')
    
    return int(angle * max_pos / max_angle)

# convert dynamixel servo position to angle
# (position between 0 and 4095)
def pos_to_angle(pos: float):
    if (pos < min_pos or pos > max_pos):
        raise Exception(f'Position must be between 0 and {max_pos}')
    
    return pos * max_angle / max_pos