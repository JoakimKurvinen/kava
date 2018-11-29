import serial 
import subprocess
import pymongo
import time #import datetime
import paho.mqtt.client as paho

broker="IoT-Cloud-Hub.azure-devices.net"

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
temp_db = myclient["tempdatabase"]
collection_1 = temp_db["temperature"]
collection_2 = temp_db["datetime"]

arduinoSerialData = serial.Serial('/dev/ttyUSB0',9600)
while 1:	 #always true
	if(arduinoSerialData.inWaiting()>0):
		sensortemp = arduinoSerialData.readline()
		sensortemp = int(sensortemp)
		print sensortemp    #Print values read from the serial output 
		
# Code for writing sensor temp in collection_1 #
# Code for writing datetime in collection_2 #
# Code for publishing dbase locally to webserver #
# Code for formatting data before sending it #
# Code for sending data to Azure $
