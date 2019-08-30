import mysql.connector
import sys

db = mysql.connector.connect(host="localhost",
                     user="root",
                     passwd="",
                     db="quran")

cursor = db.cursor()

inputSuraNumber = input("Input Sura Number:")

#cursor.execute("SELECT words.word AS id FROM words INNER JOIN sentences ON sentences.word_order AND sura_no="+inputSuraNumber)
#cursor.execute("SELECT sentences.word_order AS sentence FROM sentences WHERE sura_no="+inputSuraNumber)

cursor.execute("SELECT words.word FROM words INNER JOIN sentences ON 1=1 WHERE sentences.sura_no="+inputSuraNumber+" AND words.id IN (sentences.word_order)")
data = cursor.fetchall()

for row in data :
   print(row)

cursor.close ()

sys.exit()