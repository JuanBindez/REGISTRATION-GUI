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


import database
from tkinter import *
from tkinter import messagebox

# Cria A tabela No Banco De Dados.
database.create_table()


def insert_datas_io():
    name = input_name.get()
    age = input_age.get()
    email = input_email.get()

    database.insert_datas(name, age, email)


def to_see_database():
    database.cursor.execute("SELECT * FROM record")
    ver_db = database.cursor.fetchall()

    
    # in test DataBase
    for pessoa in ver_db:
        print(pessoa)
        #label = Label(window, text="DB" + str(pessoa)).place(x=20, y=60)
    # test DataBase


def delete_database():
    del_id = input_delete.get()
    database.delete_id(del_id)


# Initial GUI
# X é para os lados e Y é altura
window = Tk()
window.title("Registration")
window.geometry("600x600")
window['background'] = '#58F'# site to generate colors Hex:  https://www.rapidtables.com/web/color/RGB_Color.html


# Inputs
input_name = (Entry(window, width=40))
input_name.place(x=150, y=50)
label = Label(window, text="Name *").place(x=150, y=30)


input_age = (Entry(window, width=40))
input_age.place(x=150, y=100)
label = Label(window, text="Age * ").place(x=150, y=80)


input_email = (Entry(window, width=40))
input_email.place(x=150, y=150)
label = Label(window, text="Email *").place(x=150, y=130)

input_delete = (Entry(window, width=10))
input_delete.place(x=150, y=220)
label = Label(window, text=" Delete Id *").place(x=150, y=200)
# End Inputs


# Buttons
button = Button(window, text="Save", command=insert_datas_io, fg='white', bg='green')
button.place(x=210, y=400)

button = Button(window, text="See Registration", command=to_see_database, fg='white', bg='blue')
button.place(x=290, y=400)


button = Button(window, text="Delete", command=delete_database, fg='white', bg='red')
button.place(x=240, y=215)
# End Buttons
# End GUI


if __name__ == "__main__":
    window.mainloop()
