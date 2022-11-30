# Servo Control Documentation

[servos.py](/src/robot_parts/servos.py)

## Making Sure Values Are Correct

Make sure the values
```
addr_torque
addr_goal_pos
addr_curr_pos
baudate
```
are correct for the model of dynamixel servos that you are using.

Also make sure that `device_path` is correctly linked to the USB port that the servos are plugged into as well so the program can communicate with the servos.

## Functions

### Starting Up and Shutting Down Servos

<ins>**initServos()**</ins>

Inputs: Nothing
Output: Dynamixel servos become set up so you can control the servos.

**closeServos()**

Inputs: Nothing
Output: Connection to Dynamixel servos closes.

### Controlling Servos

#### Torque Control

**enableTorque(id: int) -> bool**

Inputs: id (servo id number)
Outputs: bool (whether it succeeded or not)
Attempts to turn on the torque of a servo with the inputted id value so it can be turned and hold its position.

**disableTorque(id: int) -> bool**

Inputs: id (servo id number)
Outputs: bool (whether it succeeded or not)
Attempts to disable the torque of a servo with the inputted id value so it rotates freely now and doesn't hold it's position, but also can't be told to go to a certain angle.

**torqueOn(id: int) -> bool**

Inputs: id (servo id number)
Outputs: bool (whether or not the servo with the inputted id has its torque on or off currently)

#### Rotation Control

**setAngle(id: int, angle: float) -> bool**

Inputs: id (servo id number), angle (angle to rotate servo to (0 - 359))
Outputs: bool (whether it succeeded or not)
Attempts to turn a servo with the inputted id value to the inputted angle.

**setPos(id: int, pos: int) -> bool**

Inputs: id (servo id number), pos (position to rotate servo to (0 - 4095))
Outputs: bool (whether it succeeded or not)
Attempts to turn a servo with the inputted id value to the inputted position value.

**getAngle(id: int)**

Inputs: id (servo id number)
Outputs: float (current angle of servo), bool (returns a false value if it fails to communicate with servo)
Attemps to read and return the current angle of a servo with the inputted id value.

getPos(id: int)**

Inputs: id (servo id number)
Outputs: int (current position value of servo), bool (returns a false value if it fails to communicate with servo)
Attemps to read and return the current position value of a servo with the inputted id value.