import sqlite3

con = sqlite3.connect('cinema.db')
cur = con.cursor()


cur.execute('''CREATE TABLE cinema
               (movie text, cinema text, timeslots text, class text, seats real)''')

# Event Cinema
cur.execute("INSERT INTO cinema VALUES ('eternals','event cinema','1:00pm','saver',15)")
cur.execute("INSERT INTO cinema VALUES ('eternals','event cinema','3:00pm','saver',15)")
cur.execute("INSERT INTO cinema VALUES ('eternals','event cinema','5:00pm','saver',15)")
cur.execute("INSERT INTO cinema VALUES ('eternals','event cinema','7:00pm','lux',15)")
cur.execute("INSERT INTO cinema VALUES ('eternals','event cinema','9:00pm','lux',15)")
cur.execute("INSERT INTO cinema VALUES ('eternals','event cinema','11:00pm','saver',15)")

cur.execute("INSERT INTO cinema VALUES ('no time to die','event cinema','1:00pm','saver',15)")
cur.execute("INSERT INTO cinema VALUES ('no time to die','event cinema','3:00pm','saver',15)")
cur.execute("INSERT INTO cinema VALUES ('no time to die','event cinema','5:00pm','saver',15)")
cur.execute("INSERT INTO cinema VALUES ('no time to die','event cinema','7:00pm','lux',15)")
cur.execute("INSERT INTO cinema VALUES ('no time to die','event cinema','9:00pm','lux',15)")
cur.execute("INSERT INTO cinema VALUES ('no time to die','event cinema','11:00pm','saver',15)")

cur.execute("INSERT INTO cinema VALUES ('red notice','event cinema','1:00pm','saver',15)")
cur.execute("INSERT INTO cinema VALUES ('red notice','event cinema','3:00pm','saver',15)")
cur.execute("INSERT INTO cinema VALUES ('red notice','event cinema','5:00pm','saver',15)")
cur.execute("INSERT INTO cinema VALUES ('red notice','event cinema','7:00pm','lux',15)")
cur.execute("INSERT INTO cinema VALUES ('red notice','event cinema','9:00pm','lux',15)")
cur.execute("INSERT INTO cinema VALUES ('red notice','event cinema','11:00pm','saver',15)")

# Hoyts Cinema
cur.execute("INSERT INTO cinema VALUES ('eternals','hoyts cinema','1:00pm','saver',15)")
cur.execute("INSERT INTO cinema VALUES ('eternals','hoyts cinema','3:00pm','saver',15)")
cur.execute("INSERT INTO cinema VALUES ('eternals','hoyts cinema','5:00pm','saver',15)")
cur.execute("INSERT INTO cinema VALUES ('eternals','hoyts cinema','7:00pm','lux',15)")
cur.execute("INSERT INTO cinema VALUES ('eternals','hoyts cinema','9:00pm','lux',15)")
cur.execute("INSERT INTO cinema VALUES ('eternals','hoyts cinema','11:00pm','saver',15)")

cur.execute("INSERT INTO cinema VALUES ('no time to die','hoyts cinema','1:00pm','saver',15)")
cur.execute("INSERT INTO cinema VALUES ('no time to die','hoyts cinema','3:00pm','saver',15)")
cur.execute("INSERT INTO cinema VALUES ('no time to die','hoyts cinema','5:00pm','saver',15)")
cur.execute("INSERT INTO cinema VALUES ('no time to die','hoyts cinema','7:00pm','lux',15)")
cur.execute("INSERT INTO cinema VALUES ('no time to die','hoyts cinema','9:00pm','lux',15)")
cur.execute("INSERT INTO cinema VALUES ('no time to die','hoyts cinema','11:00pm','saver',15)")

cur.execute("INSERT INTO cinema VALUES ('red notice','hoyts cinema','1:00pm','saver',15)")
cur.execute("INSERT INTO cinema VALUES ('red notice','hoyts cinema','3:00pm','saver',15)")
cur.execute("INSERT INTO cinema VALUES ('red notice','hoyts cinema','5:00pm','saver',15)")
cur.execute("INSERT INTO cinema VALUES ('red notice','hoyts cinema','7:00pm','lux',15)")
cur.execute("INSERT INTO cinema VALUES ('red notice','hoyts cinema','9:00pm','lux',15)")
cur.execute("INSERT INTO cinema VALUES ('red notice','hoyts cinema','11:00pm','saver',15)")

# Palace Cinema
cur.execute("INSERT INTO cinema VALUES ('eternals','palace cinema','1:00pm','saver',15)")
cur.execute("INSERT INTO cinema VALUES ('eternals','palace cinema','3:00pm','saver',15)")
cur.execute("INSERT INTO cinema VALUES ('eternals','palace cinema','5:00pm','saver',15)")
cur.execute("INSERT INTO cinema VALUES ('eternals','palace cinema','7:00pm','lux',15)")
cur.execute("INSERT INTO cinema VALUES ('eternals','palace cinema','9:00pm','lux',15)")
cur.execute("INSERT INTO cinema VALUES ('eternals','palace cinema','11:00pm','saver',15)")

cur.execute("INSERT INTO cinema VALUES ('no time to die','palace cinema','1:00pm','saver',15)")
cur.execute("INSERT INTO cinema VALUES ('no time to die','palace cinema','3:00pm','saver',15)")
cur.execute("INSERT INTO cinema VALUES ('no time to die','palace cinema','5:00pm','saver',15)")
cur.execute("INSERT INTO cinema VALUES ('no time to die','palace cinema','7:00pm','lux',15)")
cur.execute("INSERT INTO cinema VALUES ('no time to die','palace cinema','9:00pm','lux',15)")
cur.execute("INSERT INTO cinema VALUES ('no time to die','palace cinema','11:00pm','saver',15)")

cur.execute("INSERT INTO cinema VALUES ('red notice','palace cinema','1:00pm','saver',15)")
cur.execute("INSERT INTO cinema VALUES ('red notice','palace cinema','3:00pm','saver',15)")
cur.execute("INSERT INTO cinema VALUES ('red notice','palace cinema','5:00pm','saver',15)")
cur.execute("INSERT INTO cinema VALUES ('red notice','palace cinema','7:00pm','lux',15)")
cur.execute("INSERT INTO cinema VALUES ('red notice','palace cinema','9:00pm','lux',15)")
cur.execute("INSERT INTO cinema VALUES ('red notice','palace cinema','11:00pm','saver',15)")

con.commit()
con.close()