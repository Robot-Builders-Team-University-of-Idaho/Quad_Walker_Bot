# Leg Object Documentation

[legs.py](/src/robot_parts/legs.py)

This module contains an object to store 3 servos per robot leg in a convenient and intuitive way.

## Meta Functions

<ins>**leg(a, b, c, a_torque_on: bool = True, b_torque_on: bool = True, c_torque_on: bool = True) -> leg**</ins>

Constructor for the leg class.

Inputs:

- a: The servo closest to the center of the robot. Can either be an id integer to create a new servo object or an already existing servo object to be passed over.
- b: The servo between a and c. Can either be an id integer to create a new servo object or an already existing servo object to be passed over.
- c: The servo closest to the end of the leg / farthest away from the center of the robot. Can either be an id integer to create a new servo object or an already existing servo object to be passed over.
- a_torque_on: Whether or not you want the a joint / servo to start with its torque on.
- b_torque_on: Whether or not you want the b joint / servo to start with its torque on.
- c_torque_on: Whether or not you want the c joint / servo to start with its torque on.

Outputs:

- A leg object that stores the inputted a, b, and c servos.

<ins>**str(leg) -> str**</ins>

String caster for the leg class.

Inputs:

- A leg object

Outputs:

- A string of the leg object that says "Leg(\*self.a\*, \*self.b\*, \*self.c\*)".

## Utility

<ins>**walk(a_start_low: bool, b_increasing: bool, t: float, speed: float = 100, a_low: float = 150, a_high: float = 210, b_low: float = 130, b_high: float = 210)**</ins>

Makes the leg go to the next position to do a walking motion at time t.

Inputs:

- a_start_low = Whether the a joint on this leg should start at the low angle or the high angle.
- b_increasing = Whether the b joint begins the motion increasing its angle or not.
- t = The time (usually in microseconds) in the sine wave motion to move to.
- speed = A percentage of how fast the leg is moving in the sine wave motion.
- a_low = The lowest angle that the a joint can move to in the motion.
- a_high = The highest angle that the a joint can move to in the motion.
- b_low = The lowest angle that the b joint can move to in the motion.
- b_high = The highest angle that the b joint can move to in the motion.

Outputs:

- Makes the leg go to the next position to do a walking motion at time t.
