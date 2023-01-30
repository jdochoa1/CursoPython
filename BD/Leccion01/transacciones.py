import psycopg as bd

# Connect to the database
conexion = bd.connect(user='postgres', password='admin', host='localhost', port='5432', dbname='test_db')
try:
    #conexion.autocommit = False #valor por default

    cursor = conexion.cursor()
    sentencia = 'INSERT INTO persona(nombre, apellido, email) values (%s, %s, %s)'
    valores = ('Elver', 'Gomez', 'egomez@mail.com')
    cursor.execute(sentencia, valores)

    sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s where id_persona=%s'
    valores = ('Juan Carlos', 'Juarez', 'jcjuarez@mail.com', 1)
    cursor.execute(sentencia, valores)

    conexion.commit()
    print('Termina la transaccion, se hizo commit')
except Exception as e:
    conexion.rollback()
    print(f'Ocurrio un error, se hizo rollback: {e}')
finally:
    conexion.close()
