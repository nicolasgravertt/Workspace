import mysql.connector

midb = mysql.connector.connect(
    host='localhost',
    user='Nicolas',
    password='Hola123.',
    database='prueba'
)

cursor = midb.cursor()


sql = 'insert into Usuario(id,email,username) values (%s,%s,%s)'
values = (2,'micorreo@hotmail.com','usuarioprueba')

cursor.execute(sql,values)

midb.commit()

print(cursor.rowcount)

#cursor.execute('select * from Usuario')

#resultado = cursor.fetchall()

#print(resultado)