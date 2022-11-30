# Angle / Position Convertion Documentation

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

Inputs: angle (Angle to convert to servo position value)

Outputs: int (Servo position value that is approximately equal to the inputted angle)

<ins>**posToAngle(pos: int) -> float**</ins>

Inputs: pos (Servo position value to convert to angle)

Outputs: float (Angle that is approximately equal to the inputted position value)