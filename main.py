'''
Copyright 2022 Juan Carlos Bindez
Licensed under the Apache License, Version 2.0
'''

'''
Author: www.github.com/JuanBindez
Description: registration whith Tkinter and Sqlite3
Python Version: 3.10
Local: Brazil
'''

import os
import time
import database
from tkinter import *
from tkinter import messagebox

# Cria A tabela No Banco De Dados.
database.create_table()


def dentro_ok():

    def insert_datas_io():

        name = input_name.get()
        age = input_age.get()
        email = input_email.get()

        database.insert_datas(name, age, email)
        messagebox.showinfo("Olá", "Salvamos Para Você No Banco de Dados")


    def to_see_database():
        database.cursor.execute("SELECT * FROM record")
        ver_db = database.cursor.fetchall()
        time.sleep(3)
        messagebox.showinfo("Olá", "Foi Gerado o Arquivo resultsdatabase.txt")

        
        # genarete an file whith results of database
        file = 'resultsdatabase.txt'
        os.remove(file)
        time.sleep(5)

        with open("resultsdatabase.txt", "w") as w:
            for item in ver_db:
                w.write(str(item)+'\n')


    def delete_database():
        ask = messagebox.askyesno("Atenção!", "Este Id Será Deletado Do Banco de Dados !, Tem Certeza?")
        if ask == True:
            time.sleep(2)
            messagebox.showinfo("Olá", "Id Deletado")
            del_id = input_delete.get()
            database.delete_id(del_id)

        elif ask == False:
            pass

            
    # Initial GUI
    # X é para os lados e Y é altura
    global window

    window = Tk()
    window.title("Registration")
    window.geometry("600x600")
    window['background'] = '#262626'# site to generate colors Hex:  https://www.rapidtables.com/web/color/RGB_Color.html
    window.resizable(False, False)# False para não responsivo e True para responsivo.

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


def analisa_credenciais():
    user = input_user.get()
    password = input_pass.get()

    if user == 'admin' and password == 'admin':
        dentro_ok()

    else:
        messagebox.showinfo("Ops!", "Login Errado")


window = Tk()
window.title("Login")
window.geometry("460x280")
window['background'] = '#262626'#
window.resizable(False, False)# False para não responsivo e True para responsivo.


input_user = (Entry(window, width=20))
input_user.place(x=150, y=50)
label = Label(window, text="User *").place(x=150, y=30)

input_pass = (Entry(window, width=20))
input_pass.place(x=150, y=140)
label = Label(window, text="PassWord *").place(x=150, y=120)
    
button = Button(window, text="Entrar", command=analisa_credenciais, fg='white', bg='green')
button.place(x=210, y=210)


if __name__ == "__main__":
    window.mainloop()
