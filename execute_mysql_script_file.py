# Trying to execute a mysql script file
import mysql.connector
mycon = mysql.connector.connect(host="localhost",user="root",password="compaq@123")
mycursor = mycon.cursor()
with open('script.txt','r') as f:
    datalines = (lines.rstrip('\r\n') for lines in f)     # \r\n indicates Line feed ie end of line character
    for each in datalines:
        print(each)
        mycursor.execute(each)
        mycon.commit()

