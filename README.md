# Quad_Walker_Bot
Code and other assets for a 4-legged spider-like bot that is being built by the Mobile Robot team in the University of Idaho Robotics Club.

## Setup
To be able to run this repository on your own, you need to have the Dynamixel SDK installed on the system you want to run it on, and the right Dynamixel servos connected to your system.

Here are some links to the official Dynamixel website that show you how to download and install the Dynamixel SDK on linux:

[Downloading the Dynamixel SDK](https://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_sdk/download/)

[Installing the Python Files for the Dynamixel SDK](https://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_sdk/library_setup/python_linux/)

## Documentation

Make sure you read our [coding style standards](/docs/style_standards.md) before you start programming! Be sure to read other things in the [docs](/docs) folder as well!

When you're writing documentation, make sure the files your create are .md files. [Here's a link to a tutorial on how to make text look stylish in the markdown format](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)

## TODO

1. Test if functions in [servos.py](/src/robot_parts/servos.py) should be turned into async functions by putting a print statement before and after a function call to setAngle() that rotates a servos a lot to see how long it takes to run that function.

2. Get Robot to walk!