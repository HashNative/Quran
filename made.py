import MySQLdb
conn = MySQLdb.connect(host= "localhost",
                  user="root",
                  passwd="",
                  db="quran")
x = conn.cursor()
x.execute("SELECT *  FROM anooog1")
x.execute (" INSERT INTO anooog1 VALUES ('%s','%s') ", (188,90))
row = x.fetchall()


val = ("2", "Al-Baqarah", "2", 1, "الم","'Alif 'A', Lam 'L', Mim 'M'.","الم" )

    mycursor.execute("INSERT INTO begin1 (suraNumber, suraName, chapterNumber, sentenceNumber, sentence, meaningFor , rootWord ) VALUES ('%s','%s','%s','%s','%s','%s','%s')")
