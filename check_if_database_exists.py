# Checks if a mysql database exits
# the user is given a choice to create the database in case the database does not exist

import mysql.connector
cnx = mysql.connector.connect(host='localhost',user='root',password='compaq@123')
mycursor = cnx.cursor()
DB_NAME='Test'
try:
    mycursor.execute("USE {}".format(DB_NAME))
    print("Database switched to {}".format(DB_NAME))
except mysql.connector.Error as err:
   # print("Database {} does not exists.".format(DB_NAME))
    print(err.msg)
    choice=input("Do you want to create the database {}:".format(DB_NAME))
    if choice in ('Y','YES','YEA','y','yes','yea'):
        mycursor.execute("CREATE DATABASE {}".format(DB_NAME))
        print("Successfully created database {}".format(DB_NAME))
    else:
        print("Bye")
        exit(1)
mycursor.close()
cnx.close()



