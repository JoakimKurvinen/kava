import serial 
import subprocess
import pymongo
import datetime
import paho.mqtt.client as paho
import pprint

broker="IoT-Cloud-Hub.azure-devices.net"

client = pymongo.MongoClient("mongodb://localhost:27017/")
temp_db = client["tempdatabase"]     #tempdatabase the name of our database
posts = temp_db.posts #Collecton name

#collection_1 = temp_db["temperature"]
#collection_2 = temp_db["datetime"]

arduinoSerialData = serial.Serial('/dev/ttyUSB0',9600)
while 1:	 #always true
	if(arduinoSerialData.inWaiting()>0):
	#	sensortemp = arduinoSerialData.readline()
	#	sensortemp = int(sensortemp)
		post_data = {
			'date': datetime.datetime.now(),
			'temperature': sensortemp

		}
		result = posts.insert_one(post_data)
		print sensortemp    #Print values read from the serial output 
		
# Code for formatting data before sending it #
# Code for publishing dbase locally to webserver #
# Code for sending data to Azure $
