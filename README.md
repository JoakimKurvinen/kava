School project to make an IoT device that can take temp. input and measure a liquid's temp (in this case coffee) and send a notification when said temp. is reached.

Files:
Cgi-bin/	is the directory for the web python script (This folder is copied from /var/www/)

test/		the arduino directory for its code

arduino01.py	The main python script for accessing arduino and processing its input.

license		The license for the project code

ourmail.py 	A deprecated file (used to do our mail sending part, kept here only for historical reasons)

pseudocode.txt	A brief look at the pseudocode of arduino01.py

sensortemp.graphically.py	Another old file used to test plotting of the temp. values

values.txt 	The text file written by web python script. In our working setup this file is 
			symbolically linked to the file in /var/www/cgi-bin/values.txt 

