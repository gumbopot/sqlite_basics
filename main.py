import sqlite3, datetime, time, random

# Create connection
conn = sqlite3.connect('tutorial.db')
	# if database does not exist, this will create it

# cursor object points and performs actions similar to a real cursor
c = conn.cursor()


def create_table():
	# all caps for pure SQL commands and lower for all else
	c.execute('CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp TEXT, keyword TEXT,  value REAL)')


def data_entry():
	c.execute("INSERT INTO stuffToPlot VALUES(145123432, '2016-01-01', 'Python', 5)")

	# commit any changes
	conn.commit()
	c.close()
	conn.close()

def dynamic_data_entry():
	unix = time.time()
	date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
	keyword = 'python'
	value = random.randrange(0,10)
	c.execute("INSERT INTO stuffToPlot (unix, datestamp, keyword, value) VALUES (?, ?, ?, ?)",
	(unix, date, keyword, value))
	conn.commit()
	# don't need to open/close the connection everytime you commit


def read_from_db():
	# Select statement finds the data according to the query
	# you must then do something with the data
	#c.execute('SELECT * FROM stuffToPlot')
	c.execute("SELECT * FROM stuffToPlot WHERE unix > 1535121381")

	# data = c.fetchone()	# fetch single row
	# data = c.fetchall()

	# print(data)

	# Iterating then printing makes it much more readable
	for row in c.fetchall():
		print(row)


# create_table()
# data_entry()

# for i in range(10):
# 	dynamic_data_entry()
# 	time.sleep(1)


read_from_db()


c.close()
conn.close()
