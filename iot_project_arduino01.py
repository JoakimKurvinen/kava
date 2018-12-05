import serial 
import subprocess    #for using linux commands
import pymongo
import datetime
import paho.mqtt.client as paho
import pprint

broker="IoT-Cloud-Hub.azure-devices.net"	#Where to send our formatted data

client = pymongo.MongoClient("mongodb://localhost:27017/")
temp_db = client["tempdatabase"]     #tempdatabase the name of our database
posts = temp_db.posts 			#Collection(similar to table) name

#collection_1 = temp_db["temperature"]
#collection_2 = temp_db["datetime"]

print("The aim of this software is to record temperature in a room, format & store it in a local database and finally publish it locally and remotely\n The code is released under GPLv3")

raw_input("Press ENTER to continue")
 
arduinoSerialData = serial.Serial('/dev/ttyUSB0',9600)
while 1:	 #always true
	if(arduinoSerialData.inWaiting()>0):
	#	sensortemp = arduinoSerialData.readline()
	#	sensortemp = int(sensortemp)
		post_data = {
			'date': datetime.datetime.now(),
			'temperature': sensortemp

		}
		result = posts.insert_one(post_data)		  #Inserts data into dbase
		print sensortemp    				#Print values read from the serial output 
		pprint.pprint(posts.find_one()) 	# for testing if database is being written
		
		## Backup textfile if database stuff is hard/doesn't work ##
		f = open("temperature.txt","a+")	# Open file for writing and append to it	
		texta = subprocess.Popen("date", stdout=subprocess.PIPE)	# Using shell command 'date' to get current local time
		textb = texta.stdout.read()
		f.write("%s = " %textb)
		f.write("%d degrees\n" %sensortemp)
		f.close()

		# Code for formatting data before sending it #
	#	myquery = {'date' : datetime.datetime.now()} 	 # Return all temperatures for today (24) 
	#	mydoc = posts.find(myquery)
		
		

		# Code for publishing dbase locally to webserver #
		# Code for sending data to Azure $
