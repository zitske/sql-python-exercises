## Mostrando alguns campos da tabela de funcionários (Employees).
from connection import db

cursor = db().cursor()

query3 = '''
SELECT  EmployeeId, Firstname, Lastname
FROM Employees
LIMIT 100
;'''


cursor.execute(query3)
out=cursor.fetchall()
print(out)