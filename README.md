# Quad_Walker_Bot
Code base for a 4-legged spider-like bot named Joe the Robot (Jobo) that is being built by the Mobile Robot team in the University of Idaho Robotics Club.

## Dependencies

Here are the things you need to install for everything in this repository to work.

### Dynamixel SDK

To be able to run any code that moves the servos, you need to have the Dynamixel SDK installed on the system you want to run it on.

Here are some links to the official Dynamixel website that show you how to download and install the Dynamixel SDK on Linux:

[Downloading the Dynamixel SDK](https://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_sdk/download/)

[Installing the Python Files for the Dynamixel SDK](https://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_sdk/library_setup/python_linux/)

The servos this repository is programmed for are the XL330-M288-T servos.

### Keyboard

This is for reading key presses from the keyboard and writing key presses to the keyboard. Useful to making programs run until you press a button.

Use this command on your system to install the module:

`pip install keyboard`

Make sure you run every program that uses this module as root / sudo. Ex: `sudo python3 program.py` instead of just `python3 program.py` for Linux systems.

## Documentation

Make sure you read our [standards](/docs/standards.md) before you start adding to the repository!
Be sure to read other things in the [docs](/docs) folder as well so you can learn how to use the modules in this repo!

If you want to learn more about the Dynamixel servos to make changes to [servos.py](/src/robot_parts/servos.py) or for other purposes, check out [the control table for the Dynamixel XL330-M288-T servos](https://emanual.robotis.com/docs/en/dxl/x/xl330-m288/) that we're using for Jobo.
This will show you what all of the memory locations are for and how large each one is etc.
Be sure to also check out the Dynamixel SDK documentation for [PortHandlers](https://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_sdk/api_reference/python/python_porthandler/)
and [PacketHandlers](https://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_sdk/api_reference/python/python_packethandler/) to learn how to directly code with the Dynamixel SDK.

