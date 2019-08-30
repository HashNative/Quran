import mysql.connector
import json
import sys


db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="quran"
)

cursor = db.cursor()

inputPattern = input("***#### Create Arabic Word ####***")
inputSuraNumber = input("Input Sura Number:")
inputSuraName = input("Input Sura Name:")
inputChapterNumber = input("Input Chapter Number:")
inputSentenceNumber = input("Input Sentence Number:")
inputSentence = input("Input sentence: ")

word_order = []
for i in range(0, len(inputSentence.split(" "))):
    inputMeaning = input(str(i)+". Meaning for "+inputSentence.split(" ")[i]+":")
    inputrootWord = input("      Input root word:")

    sql = "INSERT IGNORE INTO words (word, meaning, root_word) VALUES (%s, %s, %s )"
    val = (inputSentence.split(" ")[i], inputMeaning, inputrootWord)
    cursor.execute(sql, val)
    db.commit()
    print(cursor.rowcount, "sentence inserted.")
    word_order.append(cursor.lastrowid)

sql = "INSERT INTO sentences (sura_no, sura_name, chapter_no, sentence_no, word_order) VALUES (%s,%s,%s,%s,%s)"
val = (inputSuraNumber, inputSuraName, inputChapterNumber, inputSentenceNumber, json.dumps(word_order).replace('[', '').replace(']', ''))
cursor.execute(sql, val)
db.commit()
print(cursor.rowcount, "record inserted.")

cursor.execute("SELECT word FROM words ")

data = cursor.fetchall ()

for row in data :
    print (row[0])

cursor.close ()
sys.exit()