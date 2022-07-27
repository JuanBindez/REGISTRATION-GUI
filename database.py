'''
Copyright 2022 Juan Carlos Bindez

Licensed under the Apache License, Version 2.0
'''


import sqlite3


base_db = sqlite3.connect("registration.db")
cursor = base_db.cursor()

def create_table():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS record(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        email TEXT)
        """)


def delete_id(id_del):
    cursor.execute("DELETE FROM record WHERE id=?", [id_del])
    base_db.commit()


def insert_datas(a, b, c):
    
    cursor.execute("INSERT INTO record VALUES(NULL, '"+a+"','"+b+"','"+c+"')")
    base_db.commit()#this command saves the datas in database
