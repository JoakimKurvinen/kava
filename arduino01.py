import serial 
arduinoSerialData = serial.Serial('/dev/ttyUSB1',9600)
while 1: #always true
   if(arduinoSerialData.inWaiting()>0):
      myData = arduinoSerialData.readline()
      print myData    #Print values read from the serial output 
      arduinoSerialData.write('90')    #turn servo 90 degress
