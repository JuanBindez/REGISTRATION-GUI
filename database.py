'''
Copyright 2022 Juan Carlos Bindez

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
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
