import sqlite3

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

def data_entry():
	unix = time.time()
	data = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))

