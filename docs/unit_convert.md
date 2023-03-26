# Unit Convertion Documentation

[angle_convert.py](/src/robot_parts/utils/angle_convert.py)

## Making Sure Values Are Correct

Make sure the values
```
min_angle
max_angle
min_pos
max_pos
```
are correct for the model of dynamixel servos that you are using.

## Functions

<ins>**angleToPos(angle: float) -> int**</ins>

Converts an angle value to a servo position value.

Inputs:

- angle: Angle to convert to servo position value

Outputs:

- Servo position value that is approximately equal to the inputted angle

<ins>**posToAngle(pos: int) -> float**</ins>

Converts a servo position value to an angle value.

Inputs

- pos: Servo position value to convert to angle

Outputs:

- Angle that is approximately equal to the inputted position value

<ins>**rpmToVel(rpm: float) -> int**</ins>

Converts an rpm (rotations per minute) value to a servo velocity value.

Inputs:

- rpm: Rotation per minute value to convert to a servo velocity value

Outputs:

- Servo velocity value that is approximately equal to the inputted rpm value

<ins>**velToRPM(vel: int) -> float**</ins>

Converts a servo velocity value to an rpm (rotations per minute) value.

Inputs:

- vel: Servo velocity value to convert to rpm (rotations per minute) value

Ouputs:

- RPM (rotation per minute) value that is approximately equal to the inputted velocity value