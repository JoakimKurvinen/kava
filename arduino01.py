import serial 
import subprocess
from ourmail import *


# INPUT from somewhere else	
#email
#boolean value of coffee cup-type
#temperature value 
#
#
arduinoSerialData = serial.Serial('/dev/ttyUSB0',9600)
while 1: #always true
	if(arduinoSerialData.inWaiting()>0):
		myData = arduinoSerialData.readline()
		print myData    #Print values read from the serial output 
		arduinoSerialData.write('90')    #turn servo 90 degress
#sensortemp = myData
		goaltemp = 20
		peaktemp = goaltemp + 5
		sensortemp = myData
		if sensortemp == peaktemp:  #sensortemp is myData, we need a way to read it
			if sensortemp == goaltemp:
				pass	
			#led
			#buzzer
			#servo
			#email
				#ourmail.send_email()
			else: 
				pass	
		else:
			pass		   

		break
	else:
		pass   
