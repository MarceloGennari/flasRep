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

	if state == "ON":
		ser.write('1')
	if state == "OFF":
		ser.write('0')

	time.sleep(2)
	if (ser.in_waiting > 0):
		dat = ser.read()
		print(dat)

