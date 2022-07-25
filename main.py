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


def inserir_dados_io():
    nome = entrada_nome.get()
    idade = entrada_idade.get()
    email = entrada_email.get()

    database.inserir_dados(nome, idade, email)


def ver_database():
    database.cursor.execute("SELECT * FROM cadastro")
    ver_db = database.cursor.fetchall()

    
    # in test DataBase
    for pessoa in ver_db:
        print(pessoa)
        #label = Label(window, text="DB" + str(pessoa)).place(x=20, y=60)
    # test DataBase


def delete_database():
    del_id = entrada_deletar.get()
    database.delete_id(del_id)


# Initial GUI
# X é para os lados e Y é altura
window = Tk()
window.title("Registration")
window.geometry("600x600")
window['background'] = '#58F'


# Inputs
entrada_nome = (Entry(window, width=40))
entrada_nome.place(x=150, y=50)
label = Label(window, text="Nome *").place(x=150, y=30)


entrada_idade = (Entry(window, width=40))
entrada_idade.place(x=150, y=100)
label = Label(window, text="Idade * ").place(x=150, y=80)


entrada_email = (Entry(window, width=40))
entrada_email.place(x=150, y=150)
label = Label(window, text="Email *").place(x=150, y=130)

entrada_deletar = (Entry(window, width=10))
entrada_deletar.place(x=150, y=220)
label = Label(window, text="deletar Id *").place(x=150, y=200)
# End Inputs


# Buttons
button = Button(window, text="Salvar", command=inserir_dados_io, fg='white', bg='green')
button.place(x=210, y=400)

button = Button(window, text="Ver Registro", command=ver_database, fg='white', bg='blue')
button.place(x=290, y=400)


button = Button(window, text="Deletar", command=delete_database, fg='white', bg='red')
button.place(x=240, y=215)
# End Buttons
# End GUI


if __name__ == "__main__":
    window.mainloop()
