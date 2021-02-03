#!/usr/bin/python3
import sqlite3

dbConnect = sqlite3.connect("yeniVeriTabani.db")  
dbCursor = dbConnect.cursor()  

dbCursor.execute("""SELECT * FROM musteriTablosu""")
datas = dbCursor.fetchall()
print(datas)

dbConnect.close()
