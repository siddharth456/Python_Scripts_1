# Python can be used in database applications
# One of the popular databases around is mysql
# Python needs a mysql driver to access the databases in mysql
import mysql.connector
# Creating a connection object
mycon = mysql.connector.connect(host="localhost",user="root",password="compaq@123")
# Creating a cursor object to be used for fetching result
mycursor = mycon.cursor()
# Executing a query
mycursor.execute("SHOW DATABASES")
# Getting query result
for x in mycursor:
    print(x)
