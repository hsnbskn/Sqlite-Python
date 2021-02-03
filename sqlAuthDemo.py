#!/usr/bin/python3

import sqlite3

dbConnect = sqlite3.connect('userAuthData.db')  #Veritabanina baglan.
dbCursor = dbConnect.cursor()                   #imlec olustur.

dbCursor.execute("""CREATE TABLE IF NOT EXISTS users (username,password)""")    #Kullanici adi ve parola tutan bir tablo ekle.

datas = [('admin','123456'),('hasan','2021'),('haydar','hay123dar')]            #Kullanici verileri olustur.

for data in datas:
    dbCursor.execute("""INSERT INTO users VALUES %s"""%(data,))                 #Kullanici verileri tek ogeli bir demet ile tabloya yerlestir.

dbConnect.commit()      #Verileri veritabanina isle.

userName = raw_input("Username: ")  #Kullanici adi giris
passWord = raw_input("Password: ")  #Parola giris

dbCursor.execute("""SELECT * FROM users WHERE username = '%s' AND password = '%s'"""%(userName,passWord))   #Kullanici adi ve Parolayi Veritabanindan dogrula

dataFromDb = dbCursor.fetchone()    #Bir tane veriyi al.


if dataFromDb:
    print("Login Success, welcome {}".format(dataFromDb[0]))
else:
    print("Access Denied !")






