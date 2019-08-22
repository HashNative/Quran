import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  db="quran"
)

cur = db.cursor()

cur.execute("INSERT INTO  holyquran")

inputSuraNumber = input("Input Sura Number:")
inputSuraName = input("Input Sura Name:")
inputChapterNumber = input("Input Chapter Number:")
inputSentenceNumber = input("Input Sentence Number:")
inputSentence = input("Input sentence: ")
for i in range(0, len(inputSentence.split(" "))):
    inputMeaning = input(str(i)+". Meaning for "+inputSentence.split(" ")[i]+":")
    inputMeaning = input("      Input root word:")

print(mydb)
