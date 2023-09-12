## Listando os campos de uma tabela.
from connection import db

cursor = db().cursor()

query2 = '''
PRAGMA TABLE_INFO(Products)
;'''

cursor.execute(query2)
out=cursor.fetchall()
print(out)