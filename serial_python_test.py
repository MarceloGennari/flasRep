#!/usr/bin/python
import serial
import syslog
import time
import sys
# For the motor 
port = '/dev/cu.usbmodem14311'
ser = serial.Serial(port, 9600)

def MotorSwitch(state):
	#The following line is for serial over GPIO
	state = int (state)
	ser.write(str(state + 45))


