import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="quran"
)

mycursor = mydb.cursor()

inputSuraNumber = input("Input Sura Number:")
inputSuraName = input("Input Sura Name:")
inputChapterNumber = input("Input Chapter Number:")
inputSentenceNumber = input("Input Sentence Number:")
inputSentence = input("Input sentence: ")
for i in range(0, len(inputSentence.split(" "))):
    inputMeaning = input(str(i)+". Meaning for "+inputSentence.split(" ")[i]+":")
    inputrootWord = input("      Input root word:")


    sql = "INSERT INTO begin1 (sura_number, sura_name, chapter_number, sentence_number, sentence, word, root_word) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (inputSuraNumber, inputSuraName, inputChapterNumber, inputSentenceNumber, inputSentence, inputMeaning, inputrootWord)

    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")
