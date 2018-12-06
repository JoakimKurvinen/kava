import serial 
import subprocess    #for using linux commands
import pymongo
import datetime
#import paho.mqtt.client as paho
import pprint
import json
from json2html import *

broker="IoT-Cloud-Hub.azure-devices.net"	#Where to send our formatted data

## Database Information ##
client = pymongo.MongoClient("mongodb://localhost:27017/")
temp_db = client["tempdatabase"]     #tempdatabase the name of our database
posts = temp_db.posts 			#Collection(similar to table) name


print("The aim of this software is to record temperature in a room, format & store it in a local database and finally publish it locally and remotely\n The code is released under GPLv3")

raw_input("Press ENTER to continue")
 
arduinoSerialData = serial.Serial('/dev/ttyUSB0',9600)
while 1:	 #always true
	if(arduinoSerialData.inWaiting()>0):
		sensortemp = arduinoSerialData.readline()
		sensortemp = int(sensortemp)
		post_data = {
			'date': datetime.datetime.now(),
			'temperature': sensortemp

		}
		result = posts.insert_one(post_data)		  #Inserts data into dbase
		print sensortemp    				#Print values read from the serial output 
#		for post in posts.find():		# for testing if database is being written
#			pprint.pprint(post)
		
		## Backup textfile if database stuff is hard/doesn't work ##
		f = open("temperature.txt","a+")	# Open file for writing and append to it	
		texta = subprocess.Popen("date", stdout=subprocess.PIPE)	# Using shell command 'date' to get current local time
		textb = texta.stdout.read()
		f.write("%s = " %textb)
		f.write("%d degrees\n" %sensortemp)
		f.close()

		## Code for formatting data before sending it ##
	
		subprocess.call(["mongoexport","--db", "tempdatabase", "-c", "posts", "--jsonArray", "--out", "temp.json"])  #exports our database into a file that is read in the next section


		# Code for publishing dbase locally to webserver #
		with open("temp.json", "r") as b:
			infoFromJson = json.load(b)

		html = json2html.convert(json = infoFromJson)
		htm_file = open("jsonhtml.html","w+")
		html_file.write("""
		<HTML>
		<body>
			<h1> Temperature </h1>""")
		html_file.write(html)
		html_file.write("""
		</body>
		</HTML>""")

		html_file.close
		a.close

		
		# Code for sending data to Azure $
