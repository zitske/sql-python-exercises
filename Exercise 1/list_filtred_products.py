##INNER JOIN: listando os produtos descontinuados, com as respectivas categorias.
from connection import db

cursor = db().cursor()

query4 = '''
select distinct b.*, a.CategoryName
from Categories a
inner join Products b on a.CategoryID = b.CategoryID
where b.Discontinued = '1'
;'''


cursor.execute(query4)
out=cursor.fetchall()
print(out)