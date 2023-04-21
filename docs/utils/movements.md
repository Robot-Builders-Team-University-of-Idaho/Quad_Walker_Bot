# Robot Movement Documentation

[movements.py](/src/utils/movements.py)

This module is for helping to map robotic movements to servos.

# Sine Wave Motions

<ins>**getSineAngle(t: float, lower_ang: float, upper_ang: float, start_ang: float, forward: bool, speed: float = 100, wave_len: float = 0.000013) -> float**</ins>

Returns the angle of a servo doing a sine wave motion at a given time t.
Usually used in a while loop like this:
```py
from datetime import datetime
from robot_parts.servos import *
from utils.movements import *

servo.connect()

srv = servo(1)

start_time = datetime.now()
time_passed = 0

while time_passed < 4_000_000:
	time_passed = datetime.now() - start_time # returns timedelta class
	time_passed = (time_passed.seconds * 1_000_000) + time_passed.microseconds
	angle = getSineAngle(time_passed, 135, 225, 180, True, 50)
	srv.setAngle(angle)

srv.torqueOff()
servo.close()
```
This makes a servo move in a sine wave motion between 135 degrees and 225 degrees at 50% speed with the default wave length starting at 180 degrees for 4 seconds.

Equation for sine wave:
$$\frac{upper \textunderscore ang - lower \textunderscore ang}{2} cos((speed \cdot wave \textunderscore len) t + start \textunderscore offset) + \frac{upper \textunderscore ang + lower \textunderscore ang}{2}$$

$start \textunderscore offset$ is calculated by:

```py
if forward:
```

$$start \textunderscore offset = (start \textunderscore ang - \frac{upper \textunderscore ang + lower \textunderscore ang}{2}) \cdot \frac{\pi}{upper \textunderscore ang - lower \textunderscore ang} - \frac{\pi}{2}$$

```py
else:
```

$$start \textunderscore offset = (start \textunderscore ang - \frac{upper \textunderscore ang + lower \textunderscore ang}{2}) \cdot \frac{\pi}{upper \textunderscore ang - lower \textunderscore ang} + \frac{\pi}{2}$$

Inputs:

- t: Current time in the sine wave motion, aka where on the x axis you are in the sine wave.
- lower_ang: The lowest angle in the sine wave motion (determines amplitude).
- upper_ang: The highest angle in the sine wave motion (determines amplitude).
- start_ang: The angle that the servo starts the motion at / the horizontal shift of the sine wave.
- forward = Whether or not the angle begins increasing (True) or decreasing (False) at the start (True means start increasing (shift sine wave right), False means start decreasing(shift sine wave left))
- speed: A percentage of how fast the servo is moving in the sine wave motion / a percentage of the wave_len.
- wave_len: A constant to control what a good max speed of the sine wave motion should be (default is 0.000013).

Outputs:

- The angle of a servo doing a sine wave motion at time t.

<ins>**getSinePos(t: float, lower_pos: int, upper_pos: int, start_pos: int, speed: float = 100, wave_len: float = 0.000013) -> float**</ins>

Returns the servo position of a servo doing a sine wave motion at a given time t.
Usually used in a while loop like this:
```py
from datetime import datetime
from robot_parts.servos import *
from utils.movements import *

servo.connect()

srv = servo(1)

start_time = datetime.now()
time_passed = 0

while time_passed < 4_000_000:
	time_passed = datetime.now() - start_time # returns timedelta class
	time_passed = (time_passed.seconds * 1_000_000) + time_passed.microseconds
	position = getSinePos(time_passed, 1500, 2500, 2000, True, 50)
	srv.setPos(position)

srv.torqueOff()
servo.close()
```
This makes a servo move in a sine wave motion between servo positions 1500 and 2500 at 50% speed with the default wave length starting at servo position 2000 for 4 seconds.

Equation for sine wave:
$$\frac{upper \textunderscore pos - lower \textunderscore pos}{2} cos((speed \cdot wave \textunderscore len) t + start \textunderscore offset) + \frac{upper \textunderscore pos + lower \textunderscore pos}{2}$$

$start \textunderscore offset$ is calculated by:

```py
if forward:
```

$$start \textunderscore offset = (start \textunderscore pos - \frac{upper \textunderscore pos + lower \textunderscore pos}{2}) \cdot \frac{\pi}{upper \textunderscore pos - lower \textunderscore pos} - \frac{\pi}{2}$$

```py
else:
```

$$start \textunderscore offset = (start \textunderscore pos - \frac{upper \textunderscore pos + lower \textunderscore pos}{2}) \cdot \frac{\pi}{upper \textunderscore pos - lower \textunderscore pos} + \frac{\pi}{2}$$

Inputs:

- t: Current time in the sine wave motion, aka where on the x axis you are in the sine wave.
- lower_pos: The lowest servo position in the sine wave motion (determines amplitude).
- upper_pos: The highest servo position in the sine wave motion (determines amplitude).
- start_pos: The servo position that the servo starts the motion at / the horizontal shift of the sine wave.
- forward = Whether or not the position begins increasing (True) or decreasing (False) at the start (True means start increasing (shift sine wave right), False means start decreasing(shift sine wave left))
- speed: A percentage of how fast the servo is moving in the sine wave motion / a percentage of the wave_len.
- wave_len: A constant to control what a good max speed of the sine wave motion should be (default is 0.000013).

Outputs:

- The servo position of a servo doing a sine wave motion at time t.
