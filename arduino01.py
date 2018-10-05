import serial 
import subprocess
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

#from ourmail import *		#imports our mailsend function from ourmail.py


checker = False # checks if we have already gone past the peaktemp 
send = True # checks if an email has been sent

arduinoSerialData = serial.Serial('/dev/ttyUSB0',9600)
while 1: #always true
	if(arduinoSerialData.inWaiting()>0):
		sensortemp = arduinoSerialData.readline()
		sensortemp = int(sensortemp)
		print sensortemp    #Print values read from the serial output 
		

		file = open('values.txt', 'r') #reads values from 'values' file
		email = file.readline()   #read first line
		goaltemp = file.readline() #read second line
		goaltemp = int(goaltemp)
		
		peaktemp = goaltemp + 5
		
		if sensortemp >= peaktemp:
			checker = True  
			
		
		else:
			pass	
	   
		if checker == True and sensortemp <= goaltemp:

			#buzzer and LED blink
			arduinoSerialData.write('s')    #turn servo 90 degrees and turn on the led
			#email
			#ourmail.send_email()
			if send == True:
				fromaddr = "" #email here
				msg = MIMEMultipart()
				msg['From'] = fromaddr
				msg['To'] = email
				msg['Subject'] = "Your coffee is ready"
				body = "Your coffee is ready at temperature %s C" % (goaltemp) 
				msg.attach(MIMEText(body, 'plain'))
				server = smtplib.SMTP('smtp.gmail.com', 587)
				server.starttls()
				server.login(fromaddr, "")    #password here 
				text = msg.as_string(email)
				server.sendmail(fromaddr, email, text)
				server.quit()
				send = False
			else:
				pass

		else:
			pass
				
	else:
		pass   
