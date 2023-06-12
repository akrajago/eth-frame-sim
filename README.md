# Ethernet Frame Forwarding Simulator

### Introduction
Welcome to this Ethernet frame simulator! It's still a work in progress; the details below will illustrate its current capabilities. This project was developed in Python using the tkinter module to create a GUI.

Known bugs:
- "Add device" button shows up when router is clicked after sending a few Ethernet frames

### Installation

1) To use this application, clone this repository with the command:  
`git clone git@github.com:akrajago/eth-frame-sim.git`
2) Next, run `project.py` in an IDE or navigate to the newly created directory in your terminal and run `python3 project.py`
    - NOTE: this project was created with Python 3.9

### Usage
NOTE: since this application is still in the development phase, it has not been configured with error checking/handling; attempting to add multiple devices to a single port or giving two devices the same name will result in the application not working properly
- Router:  
  - NOTE: the application has been hardcoded to only support a single network at this time
  - Click the router to display its port information
  - Double click the router to create an Ethernet frame originating from it
- Switch:
  - Click a switch to display its port information and MAC address table
    - NOTE: the MAC address table does not update dynamically; you must click the switch again to view its current status
  - Click the "add device" button to add a PC or switch to one of the switch's ports
- PC:
  - Double click a PC to create an Ethernet frame originating from  it