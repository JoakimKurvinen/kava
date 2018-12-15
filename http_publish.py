def local_publish_http():    
    with open('temperature.txt', 'r') as f:
            temp_list = []
            for line in f:
                    temp_list.append(line)

    with open('html_table.html', 'w') as f:
            f.write("""
    <html>

    <head>

    <style>

    table {

      font-family: arial, sans-serif;

      border-collapse: collapse;

      width: 100%;

    }



    td, th {

      border: 1px solid #dddddd;

      text-align: left;

      padding: 8px;

    }



    tr:nth-child(even) {

      background-color: #dddddd;

    }

    </style>

    </head>

    <body>



    <h2>Temperature Recordings</h2>
                    


    <table>

      <tr>

        <th>Temperature</th>

        <th>Time</th>
     </tr>""")
            counter = 1
            for i in temp_list:
                    if counter % 2 != 0:
                            f.write('<tr>')
                    string = '<td>' + str(i) + '</td>'
                    f.write(string)
                    if counter % 2 == 0:
                            f.write('</tr>')
                    counter = counter + 1
            f.write("""
    </table>

    </body>

    </html>""")




