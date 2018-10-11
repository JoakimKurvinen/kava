#!/usr/bin/python

# Import modules for CGI and OS
import cgi, cgitb, os

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields and convert them to string
toaddr = form.getvalue('email')
temperature  = form.getvalue('temperature')
toaddr = str(toaddr)
temperature = str(temperature)

# Create a file for the values
file = open("values.txt", "w")
file.write(toaddr + '\n')
file.write(temperature)
file.close()

# Type of coffee cup
# if form.getvalue('cup'):
#     cup = form.getvalue('cup')
# else:
#     cup = "Not set"

# Web page content
print "Content-type:text/html\r\n\r\n"
print '<html>'
print '<head>'
print '<title>Coffee thing</title>'
print '</head>'
print '<body>'
print "E-mail address is: %s" % (toaddr)
print '</p>'
print "Temperature is: %s" % (temperature)
print '</body>'
print '</html>'
