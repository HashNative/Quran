import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="quran"
)

mycursor = mydb.cursor()


mycursor.execute("CREATE TABLE customersererer (name VARCHAR(255), address VARCHAR(255))")


mycursor.execute("SHOW TABLES")

for x in mycursor:
     print(x)
