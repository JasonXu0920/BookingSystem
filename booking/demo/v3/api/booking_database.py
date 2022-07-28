import sqlite3

con = sqlite3.connect('booking.db')
cur = con.cursor()


cur.execute('''CREATE TABLE booking
               (cinema text, username text, movie text, time text, number real)''')

con.commit()
con.close()