import mysql.connector

mydb = mysql.connector.connect(
    host='10.76.245.196',
    user='root',
    password='Password123!'
)
print(mydb)
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")
for i in mycursor:
    print(i)


