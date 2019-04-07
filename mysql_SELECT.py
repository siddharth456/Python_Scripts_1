# execute a SELECT statement in mysql
import mysql.connector
mycon = mysql.connector.connect(host="localhost",user="root",password="compaq@123",database="world")
mycursor = mycon.cursor()
mycursor.execute("select * from city where District='Bihar'")
# fetchall() method gets all rows from the last executed statement
# use the fetchone() method if you want only 1 row
myresult = mycursor.fetchall()
for x in myresult:
    print(x)