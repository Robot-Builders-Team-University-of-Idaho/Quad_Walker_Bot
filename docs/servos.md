# Servo Control Documentation

[servos.py](/src/robot_parts/servos.py)

# Making Sure Values Are Correct

Make sure the values
```
addr_torque
addr_goal_pos
addr_curr_pos
baudate
```
are correct for the model of dynamixel servos that you are using.

The model we are currently using is the [XL330-M288-T](https://emanual.robotis.com/docs/en/dxl/x/xl330-m288/)

Also make sure that `device_path` is correctly linked to the USB port that the servos are plugged into as well so the program can communicate with the servos.

# Servo Class

## Functions

### Starting Up and Shutting Down Servos

<ins>**servo.initServos()**</ins>

Opens connection to Dynamixel servos so they can be controlled and interacted with.

Inputs:

Output:

<ins>**servo.closeServos()**</ins>

Closes the connection to the Dynamixel servos.

Inputs:

Output:

<ins>**servo(id: int, torqueOn: bool = True) -> servo**</ins>

Constructor for servo class.

Inputs:

- id: ID value of a servo.
- torqueOn: Whether or not the torque should be enabled upon construction (true by default).

Outputs:

- A servo object with the inputted ID value.

<ins>**str(servo) -> str**</ins>

String caster for servo class.

Inputs:

- Servo object.

Outputs:

- String that says "Servo \*self.id\*".

<ins>**del**</ins>

Destructor for servo class. Disables the servo's torque when called.

### Controlling Servos

#### Torque Control

<ins>**servo.enableTorque() -> bool**</ins>

Turns on the torque of a servo (this will make it so the servo can move and hold it's position).

Inputs:

Outputs:

- True if the communication with the servo succeeded, false if it didn't.

<ins>**servo.disableTorque() -> bool**</ins>

Turns off the torque of a servo (this will make it so the servo will be loose and no longer hold it's position, as well as disable movement control).

Inputs:

Outputs:

- True if the communication with the servo succeeded, false if it didn't.

<ins>**servo.torqueOn() -> bool**</ins>

Returns true if a servo's torque is on or false if it's not.

Inputs:

Outputs:

- True if the servo's torque is on, false if it's not or if the communication with the servo failed.

#### Rotation Control

<ins>**servo.setAngle(angle: float) -> bool**</ins>

Turns a servo to a specific angle between 0 and 359 degrees.

Inputs:

- angle: Angle to rotate servo to (0 - 359).

Outputs:

- True if the inputted value was valid and the communication with the servo succeeded, false otherwise.

<ins>**servo.setPos(pos: int) -> bool**</ins>

Turns a servo to a specific position value between 0 and 4095.

Inputs:

- pos: Position to rotate servo to (0 - 4095).

Outputs:

- True if the inputted value was valid and the communication with the servo succeeded, false otherwise.

<ins>**servo.getAngle()**</ins>

Returns the current angle of a servo.

Inputs:

Outputs:

- Current angle of servo.

or

- False if communication with the servo fails.

<ins>**servo.getPos()**</ins>

Returns the current position value of a servo.

Inputs:

Outputs:

- Current position value of servo.

or

- False if communication with the servo fails.

<ins>**servo.waitForAngle(angle: float, error: float = 100):

Stalls the program until a servo reaches the inputted angle (or comes close enough, defined by the error input).

Inputs:

- angle: Angle to wait for servo to reach.
- error: Number of position values away from the inputted angle that the servo can be for the function to end. Default is 100.

Outputs:

- Returns false if the inputted angle is not between 0 and 359.

<ins>**servo.waitForPos(pos: int, error: float = 100):

Stalls the program until a servo reaches the inputted position value (or comes close enough, defined by the error input).

Inputs:

- pos: Position value to wait for servo to reach.
- error: Number of position values away from the inputted position value that the servo can be for the function to end. Default is 100.

Outputs:

- Returns false if the inputted position value is not between 0 and 4095.

#### Speed Control

<ins>**setRPM(rpm: float) -> bool**</ins>

Sets the max speed a servo turns at in RPM units (rotations per minue). Min is 0.229, max is 103.

Inputs:

- rpm: Max rotations per minute that the servo will rotate at (0.229 to 103).

Outputs:

- True if the inputted value was valid and the communication with the servo succeeded, false otherwise.

<ins>**setVel(vel: int) -> bool**</ins>

Sets the max speed a servo turns at in servo velocity units. Min is 1, max is 450.

Inputs:

- vel: Max servo velocity units that the servo will rotate at (1 to 450).

Outputs:

- True if the inputted value was valid and the communication with the servo succeeded, false otherwise.
