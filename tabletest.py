
temp = [['4 Dec 2018 1130', '23'],['5 Dec 2018 2200', '21']]

cols = ["<td>{0}</td>".format( "</td><td>".join(t) ) for t in temp]

rows = "<tr>{0}</tr>".format( "</tr>\n<tr>".join(cols) )

f = open("table_test.html", "w+")
f.write("""
<HTML>
<body>
	<h1> Temperature </h1>
	<table>
	{0}
	</table>
</body>
</HTML>""".format(rows))

f.close




