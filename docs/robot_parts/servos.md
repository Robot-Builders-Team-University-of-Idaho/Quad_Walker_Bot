# Servo Control Documentation

[servos.py](/src/robot_parts/servos.py)

# Making Sure Values Are Correct

Make sure the values
```
addr_torque
addr_goal_pos
addr_curr_pos
addr_pro_vel
addr_curr_vel
addr_pro_acl
baudate
```
are correct for the model of dynamixel servos that you are using.

The model we are currently using is the [XL330-M288-T](https://emanual.robotis.com/docs/en/dxl/x/xl330-m288/).

Also make sure that `device_path` is correctly linked to the USB port that the servos are plugged into as well so the program can communicate with the servos.

# Servo Class

## Starting Up and Shutting Down Servos

<ins>**servo.connect()**</ins>

Opens connection to Dynamixel servos so they can be controlled and interacted with.

Inputs:

Output:

<ins>**servo.close()**</ins>

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

<ins>**del**</ins>

Destructor for servo class. Disables the servo's torque when called.

## Utility

<ins>**str(servo) -> str**</ins>

String caster for servo class.

Inputs:

- Servo object.

Outputs:

- String that says "Servo(\*self.id\*)".

<ins>**servo.\_\_commErrorCheck(result, error, func_name: str) -> bool**</ins>

Checks for errors from a communication attempt with a servo.

Inputs:

- result: The result value of a communication with a servo.
- error: The error value of a communication with a servo.
- func_name: The name of the function that is currently checking the communication (so the error message can say where is happened if there is an error).

Outputs:

- True if there were no errors with the communication attempt.
- False if there was an error with the communication attempt.

## Torque Control

<ins>**servo.torqueOn() -> bool**</ins>

Turns on the torque of a servo (this will make it so the servo can move and hold it's position).

Inputs:

Outputs:

- True if the communication with the servo succeeded, false if it didn't.

<ins>**servo.torqueOff() -> bool**</ins>

Turns off the torque of a servo (this will make it so the servo will be loose and no longer hold it's position, as well as disable movement control).

Inputs:

Outputs:

- True if the communication with the servo succeeded, false if it didn't.

<ins>**servo.torqueIsOn() -> bool**</ins>

Returns true if a servo's torque is on or false if it's not.

Inputs:

Outputs:

- True if the servo's torque is on, false if it's not or if the communication with the servo failed.

<ins>**servo.torqueIsOff() -> bool**</ins>

Returns true if a servo's torque is off or false if it's not.

Inputs:

Outputs:

- True if the servo's torque is off, false if it's not or if the communication with the servo failed.

## Rotation Control

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

- Current angle of the servo if the communication succeeds, false otherwise.

<ins>**servo.getPos()**</ins>

Returns the current position value of a servo.

Inputs:

Outputs:

- Current position value of the servo if the communication succeeds, false otherwise.

<ins>**servo.waitForAngle(angle: float, error: float = 100)**</ins>

Stalls the program until a servo reaches the inputted angle (or comes close enough, defined by the error input).

Inputs:

- angle: Angle to wait for servo to reach.
- error: Number of position values away from the inputted angle that the servo can be for the function to end. Default is 100.

Outputs:

<ins>**servo.waitForPos(pos: int, error: float = 100)**</ins>

Stalls the program until a servo reaches the inputted position value (or comes close enough, defined by the error input).

Inputs:

- pos: Position value to wait for servo to reach.
- error: Number of position values away from the inputted position value that the servo can be for the function to end. Default is 100.

Outputs:

## Speed Control

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

<ins>**getRPM()**</ins>

Returns the current speed of a servo in rpm (rotations per minute).

Inputs:

Outputs:

- Current rpm of the servo if the communication succeeds, false otherwise.

<ins>**getVel()**</ins>

Returns the current speed of a servo in servo velocity units.

Inputs:

Outputs:

- Current velocity value of the servo if the communication succeeds, false otherwise.

## Acceleration Control

<ins>**setRPM2(rpm2: float) -> bool**</ins>

Sets the acceleration of a servo in RPM^2 (rotations per minute squared) units. Min is 214.577, max is 7,031,044.56.

Inputs:

- rpm2: The speed at which a servo will reach max speed and slow down to a stop while rotating / changing position.

Outputs:

- True if the inputted value was valid and the communication with the servo succeeded, false otherwise.

<ins>**setAccel(accel: int) -> bool**</ins>

Sets the acceleration of a servo. Min is 1, max is 32,767.

Inputs:

- accel: The speed at which a servo will reach max speed and slow down to a stop while rotating / changing position.

Outputs:

- True if the inputted value was valid and the communication with the servo succeeded, false otherwise.
