import serial

arduinoSerialData = serial.Serial('/dev/ttyUSB0',9600)
while 1: #always true
	if(arduinoSerialData.inWaiting()>0):
		sensortemp = arduinoSerialData.readline()
		sensortemp = int(sensortemp)
		print sensortemp    #Print values read from the serial output 
