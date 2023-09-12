import sqlite3

banco = sqlite3.connect('Exercise 2/base.db')
cursor = banco.cursor()

query = '''
SELECT  * FROM clientes
;'''

cursor.execute(query)
out=cursor.fetchall()
print(out)



#Obtém a média da idades, por meio do SQL diretamente:

query = '''
SELECT  avg(age) FROM clientes
;'''

cursor.execute(query)
out=cursor.fetchall()
print(out)