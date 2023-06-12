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

### Example Cases
1) Sending Ethernet frames in a network with a single router
   - NOTE: each entry stays in the MAC table for 30 seconds (change `self.timer` in `Switch.py` to modify this), and you must click the switch again to see the table's current status

Let's start by adding 3 PCs to Switch 1: PC-A, PC-B, and PC-C.  
***Frame 1: PC-A to Router***  
Since Router's MAC address isn't in Switch 1's MAC address table, it sends the frame as an unknown unicast. We can see that Switch 1's MAC address table now contains Router's MAC address.  
Let's now send a response frame from Router to PC-A  
***Frame 2: Router to PC-A***   
As we can see, Switch 1's MAC address table now contains the MAC addresses for both PC-A and Router.  
Let's send a frame from PC-A to PC-B.  
***Frame 3: PC-A to PC-B***  
Since PC-B isn't in Switch 1's MAC address table, it sends the frame out as an unknown unicast. As expected, the timer for PC-A's entry is reset.    
Like before, let's send a response back, this time from PC-B to PC-A.  
***Frame 4: PC-B to PC-A***  
Since PC-B is not in Switch 1's MAC address table, it gets added. Since PC-A is already in the table, the frame travels from PC-A to PC-B without going to PC-C or Router.  
Finally, let's let the entry for Router expire.  
***Frame 5: PC-A to Router***   
Now, when we send a frame from PC-A to Router, it is again sent as an unknown unicast.