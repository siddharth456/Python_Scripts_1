# When query values are provided by user,you should escape the values.
# This is to prevent SQL injections, which is a common web hacking technique to destroy or misuse a database
import mysql.connector
mycon = mysql.connector.connect(host='localhost',user='root',password='compaq@123',database='world')
mycursor = mycon.cursor()
# Escape query values using a placeholder %s
sql = "select * from city where CountryCode = %s and Population > %s;"
arg = ['USA',1500000]   # We can use a list or a tuple
mycursor.execute(sql,arg)
myresult = mycursor.fetchall()
# rowcount(read only) property returns the number of rows for SELECT statements or the number of rows
# affected by DML statements like INSERT or UPDATE or DELETE
print(mycursor.rowcount,"records matched")
for x in myresult:
    print(x)
mycon.close()

