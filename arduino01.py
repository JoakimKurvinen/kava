import serial 
arduinoSerialData = serial.Serial('/dev/ttyUSB1',9600)
while 1:
   if(arduinoSerialData.inWaiting()>0):
      myData = arduinoSerialData.readline()
      print myData
      arduinoSerialData.write('180')
