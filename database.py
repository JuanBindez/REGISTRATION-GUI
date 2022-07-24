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


banco_db = sqlite3.connect("data_base_registration.db")
cursor = banco_db.cursor()

def create_table():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cadastro(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        idade INTEGER,
        email TEXT)
        """)


def delete_id(id_del):
    cursor.execute("DELETE FROM cadastro WHERE id=?", [id_del])
    banco_db.commit()


def inserir_dados(i, g, h):
    
    cursor.execute("INSERT INTO cadastro VALUES(NULL, '"+i+"','"+g+"','"+h+"')")
    banco_db.commit()#este comando salva os dados no banco de dados