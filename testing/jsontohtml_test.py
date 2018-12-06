from json2html import *
import json

with open("temp_test.json", "r") as f:
	infoFromJson = json.load(f)

#infoFromJson = json.loads(f)
#print json2html.convert(json = infoFromJson)
#print json2html.convert(json = f)
html = json2html.convert(json = infoFromJson)

html_file = open("jsonhtml.html","w+")
html_file.write("""
<HTML>
<body>
	<h1> Temperature </h1>""")
html_file.write(html)
html_file.write("""
</body>
</HTML>""")

html_file.close

f.close
