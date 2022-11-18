# Quad_Walker_Bot
Code and other assets for a 4-legged spider-like bot that is being built by the Mobile Robot team in the University of Idaho Robotics Club.

## Setup
To be able to run this repository on your own, you need to have the Dynamixel SDK installed on the system you want to run it on, and the right Dynamixel servos connected to your system.

Here are some links to the official Dynamixel website that show you how to download and install the Dynamixel SDK on linux:

[Downloading the Dynamixel SDK](https://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_sdk/download/)
[Installing the Python Files for the Dynamixel SDK](https://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_sdk/library_setup/python_linux/)

In servo_control.py, make sure the address values are correct for the dynamixel servos that you are using, and that the device path is correct as well.

In angle_convert.py, make sure the min and max angle and position values are correct for the dynamixel servos that you are using.