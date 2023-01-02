# Quad_Walker_Bot
Code and other assets for a 4-legged spider-like bot named Joe the Robot (Jobo) that is being built by the Mobile Robot team in the University of Idaho Robotics Club.

## Setup
To be able to run this repository on your own, you need to have the Dynamixel SDK installed on the system you want to run it on, and the right Dynamixel servos connected to your system.

Here are some links to the official Dynamixel website that show you how to download and install the Dynamixel SDK on linux:

[Downloading the Dynamixel SDK](https://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_sdk/download/)

[Installing the Python Files for the Dynamixel SDK](https://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_sdk/library_setup/python_linux/)

## Documentation

Make sure you read our [coding style standards](/docs/style_standards.md) before you start programming! Be sure to read other things in the [docs](/docs) folder as well!

## TODO

1. Test if functions in [servos.py](/src/robot_parts/servos.py) should be turned into async functions by putting a print statement before and after a function call to setAngle() that rotates a servos a lot to see how long it takes to run that function.

2. Get Jobo to do squats