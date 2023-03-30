# Unit Convertion Documentation

[angle_convert.py](/src/robot_parts/utils/angle_convert.py)

## Making Sure Values Are Correct

Make sure the values
```
min_angle
max_angle
min_pos
max_pos

min_rpm
max_rpm
min_vel
max_vel

min_rpm2
max_rpm2
min_accel
max_accel
```
are correct for the model of dynamixel servos that you are using.

## Functions

<ins>**angleToPos(angle: float) -> int**</ins>

Converts an angle value to a servo position value.

Inputs:

- angle: Angle to convert to servo position value.

Outputs:

- Servo position value that is approximately equal to the inputted angle.

<ins>**posToAngle(pos: int) -> float**</ins>

Converts a servo position value to an angle value.

Inputs

- pos: Servo position value to convert to angle.

Outputs:

- Angle that is approximately equal to the inputted position value.

<ins>**rpmToVel(rpm: float) -> int**</ins>

Converts an rpm (rotations per minute) value to a servo velocity value.

Inputs:

- rpm: Rotation per minute value to convert to a servo velocity value.

Outputs:

- Servo velocity value that is approximately equal to the inputted rpm value.

<ins>**velToRPM(vel: int) -> float**</ins>

Converts a servo velocity value to an rpm (rotations per minute) value.

Inputs:

- vel: Servo velocity value to convert to rpm (rotations per minute) value.

Ouputs:

- RPM (rotations per minute) value that is approximately equal to the inputted velocity value.

<ins>**rpm2ToAccel(rpm2: float) -> int**</ins>

Converts an rpm^2 (rotations per minute squared) value to a servo acceleration value.

Inputs:

- rpm2: Rotation per minute squared value to convert to a servo acceleration value.

Outputs:

- Servo acceleration value that is approximately equal to the inputted rpm2 value.

<ins>**accelToRPM2(accel: int) -> float**</ins>

Converts a servo acceleration value to an rpm^2 (rotations per minute squared) value.

Inputs:

- accel: Servo acceleration value to convert to rpm^2 (rotations per minute squared) value.

Outputs:

- RPM^2 (rotations per minute squared) value that is approximately equal to the inputted acceleration value.
