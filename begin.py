import mysql.connector


db = mysql.connector.connect(host="localhost",
                     user="root",
                     passwd="",
                     db="quran")


cur = db.cursor()

cur.execute("SELECT * FROM holyquran")


for row in cur.fetchall():
    print (row [4])



