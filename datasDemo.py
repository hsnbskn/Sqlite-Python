#!/usr/bin/python3
import sqlite3

dbConnect = sqlite3.connect("yeniVeriTabani.db")  
dbCursor = dbConnect.cursor()    

datas = [('Altar','Turkboy','Asker','Sogut'),('Adem','Kara','Doktor','Rize'),('irem','Burgaz','ogretmen','Antalya')]

dbCursor.execute("""CREATE TABLE IF NOT EXISTS musteriTablosu (isim,soyisim,meslek,memleket)""")

for data in datas:
    dbCursor.execute("""INSERT INTO musteriTablosu VALUES (?,?,?,?)""", data)

dbConnect.commit()
dbConnect.close()

