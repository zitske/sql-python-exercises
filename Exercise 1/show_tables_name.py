## Teste
from connection import db

cursor = db().cursor()

query1='''SELECT Name
                        FROM sqlite_master
                        WHERE type='table';'''

cursor.execute(query1)
out=cursor.fetchall()
print(out)