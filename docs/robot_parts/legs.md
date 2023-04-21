# Leg Object Documentation

[legs.py](/src/robot_parts/legs.py)

This module contains an object to store 3 servos per robot leg in a convenient and intuitive way.

Check out [servos.md](/docs/robot_parts/servos.md) for more information on how to control the servos and [movements.md](/docs/utils/movements.md) for more information on how the getSineAngle() function works.

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

Usually used like this:

```py
from datetime import datetime
from robot_parts.legs import *

servo.connect()

lg = leg(1, 2, 3)

a_low = 150
a_high = 210
b_low = 130
b_high = 210
b_mid = (b_low + b_high) / 2

lg.a.setAngle(a_high)
lg.b.setAngle(b_mid)
lg.c.setAngle(90)

start_time = datetime.now()
time_passed = 0

while time_passed < 4_000_000:
	time_passed = datetime.now() - start_time # returns timedelta class
	time_passed = (time_passed.seconds * 1_000_000) + time_passed.microseconds
	lg.walk(False, True, time_passed, speed=50, a_low=a_low, a_high=a_high, b_low=b_low, b_high=b_high)

lg.a.torqueOff()
lg.b.torqueOff()
lg.c.torqueOff()
servo.close()
```

This makes a leg made of servos 1, 2, and 3 move in a walking motion with the a joint starting at its highest angle in the motion, with b increasing its angle at the start, with the a joint moving between 150 and 210 degrees,
with the b joint moving between 170 and 210 degrees (b joint never goes below the mid point between low and high to form a half-circle motion to be able to walk), and at 50% speed for 4 seconds.

Make sure to start the a servo at either the highest or lowest point in the movement corresponding to the a_start_low value that you choose.
Also be sure to start the b servo at the mid point between the b_low and b_high values.
Doing this will make it so these joints won't jolt over to where they're supposed to be at the start instead of just already being there.

Note: The b servo will never go below the mid point between the b_low and b_high movement so it forms a half-circle motion to be able to walk.

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
