#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sqlite3

dbConnect = sqlite3.connect("yeniVeriTabani.db")    #bağlantı kur.
dbCursor = dbConnect.cursor()                       #imleç oluştur.

tableCreate = """CREATE TABLE IF NOT EXISTS musteriTablosu (isim,soyisim,meslek,memleket)"""
insertValuesInTable = """INSERT INTO musteriTablosu VALUES ("Hasan","Baskın","Adli Bilişim Mühendisi","Antalya") """

dbCursor.execute(tableCreate)           #tablo oluştur.
dbCursor.execute(insertValuesInTable)   #tabloya değerleri ekle.
dbConnect.commit()                       #verilerin veritabanına işlenmesi.

dbConnect.close()   #bağlantıyı kes.