## Criação de uma tabela de clientes, com API de importação de dados.
import sqlite3

banco = sqlite3.connect('Exercise 2/base.db')
cursor = banco.cursor()
cursor.execute('CREATE TABLE clientes (id text , pnome text, unome text, email text,age int)')  # cria uma tabela no banco
banco.commit()  # salva


import requests
response = requests.get("https://randomuser.me/api/").json()

#mostrar os valores aleatórios obtidos, nos seus respectivos campos:
print(response['results'][0])

#obter os campos de interesse para 20 clientes:
for i in range(20):
    response = requests.get("https://randomuser.me/api/").json()
    identif=response['results'][0]['id']['value']
    primeiro_nome=response['results'][0]['name']['first']
    ultimo_nome=response['results'][0]['name']['last']
    email=response['results'][0]['email']
    idade=int(response['results'][0]['dob']['age'])
   
    if not (identif is None):
         # insere os valores
        cursor.execute('INSERT INTO clientes VALUES ("'+ identif+'","'+ primeiro_nome+'","'+ultimo_nome+'","'+email +'",'+str(idade)+')' ) 
   

banco.commit()  # salva os dados