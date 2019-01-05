import pandas as pd

columns = ['date', 'temperature']
df = pd.read_csv('csv.csv', names=columns)

# This you can change it to whatever you want to get
age_15 = df[df['age'] == 'U15']
# Other examples:
bye = df[df['opp'] == 'Bye']
crushed_team = df[df['ACscr'] == '0']
crushed_visitor = df[df['OPPscr'] == '0']
# Play with this

# Use the .to_html() to get your table in html
elo=print(crushed_visitor.to_html())

file = open("csvhtml.test","w+")
file.write(elo)
file.close()
