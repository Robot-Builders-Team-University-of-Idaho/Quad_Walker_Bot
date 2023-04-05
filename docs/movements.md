# Robot Movement Documentation

[movements.py](/src/utils/movements.py)

# Sine Wave Motions

<ins>**getSineAngle(t: float, lower_ang: float, upper_ang: float, start_ang: float, speed: float = 100, wave_len: float = 0.000013) -> float**</ins>

Returns the angle of a servo doing a sine wave motion at a given time t.
Usually used in a while loop like this:
```py
start_time = datetime.now()
time_passed = 0

while time_passed < 4_000_000:
	time_passed = datetime.now() - start_time # returns timedelta class
	time_passed = (time_passed.seconds * 1_000_000) + time_passed.microseconds
	angle = getSineAngle(time_passed, 135, 225, 180, 50)
	servo.setAngle(angle)
```
This makes a servo move in a sine wave motion between 135 degrees and 225 degrees at 50% speed with the default wave length starting at 180 degrees for 4 seconds.

Equation for sine wave:
$$\frac{upperang - lowerang}{2} sin((speed \cdot wavelen) t + startangoffset) + \frac{upperang + lowerang}{2}$$

Inputs:

- t: Current time in the sine wave motion, aka where on the x axis you are in the sine wave.
- lower_ang: The lowest angle in the sine wave motion (determines amplitude).
- upper_ang: The highest angle in the sine wave motion (determines amplitude).
- start_ang: The angle that the servo starts the motion at / the horizontal shift of the sine wave.
- speed: A percentage of how fast the servo is moving in the sine wave motion / a percentage of the wave_len.
- wave_len: A constant to control what a good max speed of the sine wave motion should be (default is 0.000013).

Outputs:

- The angle of a servo doing a sine wave motion at time t.

<ins>**getSinePos(t: float, lower_pos: int, upper_pos: int, start_pos: int, speed: float = 100, wave_len: float = 0.000013) -> float**</ins>

Returns the servo position of a servo doing a sine wave motion at a given time t.
Usually used in a while loop like this:
```py
start_time = datetime.now()
time_passed = 0

while time_passed < 4_000_000:
	time_passed = datetime.now() - start_time # returns timedelta class
	time_passed = (time_passed.seconds * 1_000_000) + time_passed.microseconds
	position = getSinePos(time_passed, 1500, 2500, 2000, 50)
	servo.setPos(position)
```
This makes a servo move in a sine wave motion between servo positions 1500 and 2500 at 50% speed with the default wave length starting at servo position 2000 for 4 seconds.

Equation for sine wave:
$$\frac{upperpos - lowerpos}{2} sin((speed \cdot wavelen) t + startposoffset) + \frac{upperpos + lowerpos}{2}$$

Inputs:

- t: Current time in the sine wave motion, aka where on the x axis you are in the sine wave.
- lower_pos: The lowest servo position in the sine wave motion (determines amplitude).
- upper_pos: The highest servo position in the sine wave motion (determines amplitude).
- start_pos: The servo position that the servo starts the motion at / the horizontal shift of the sine wave.
- speed: A percentage of how fast the servo is moving in the sine wave motion / a percentage of the wave_len.
- wave_len: A constant to control what a good max speed of the sine wave motion should be (default is 0.000013).

Outputs:

- The servo position of a servo doing a sine wave motion at time t.
