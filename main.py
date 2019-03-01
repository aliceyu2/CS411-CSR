#!/usr/bin/python
import MySQLdb

# Function for connecting to the MySQL database
def mySQLConnect():
	try:
		# Open the database connection
		conn = MySQLdb.connect("localhost", "root", "myPassword", "CSR")
		print("A MySQL connection has been opened!")
		return conn
	except MySQLdb.Error as err:
		print("Error while connecting to the MySQL database!", err)
		return 0

# Function to test if the database connection works as intended
def testSQLConnection(conn):
	# Make a Cursor object for query execution
	cursor = conn.cursor()
	# Execute SQL query
	cursor.execute("SELECT * FROM Profile")
	# Fetch all of the data from the previously executed query
	profileData = cursor.fetchall()
	# Find the total number of rows in the Profile table
	cursor.execute("SELECT COUNT(*) FROM Profile")
	profileRows = cursor.fetchone()
	# Find the total number of columns in the Profile table
	cursor.execute("SELECT COUNT(*) FROM INFORMATION_SCHEMA.COLUMNS WHERE table_schema = 'CSR' AND table_name = 'Profile'")
	profileColumns = cursor.fetchone()
	''' Print contents of the Profile table '''
	i = 0
	j = 0
	for i in range(profileRows[0]):
		print('Row', i)
		for j in range(profileColumns[0]):
			print('profileData(', i, j, '): ', profileData[i][j])

def mySQLDisconnect(conn):
	# Close the database connection
	conn.close()
	print("The MySQL connection is closed!")

''' Script starts here '''
# Connect to the MySQL database
myConnection = mySQLConnect()
# Test the connection
testSQLConnection(myConnection)
# Call the search function
import search
# Disconnect from the MySQL database
mySQLDisconnect(myConnection)
