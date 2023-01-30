import pymysql

# Connect to the database
conexion = pymysql.connect(host='localhost',
                             user='root',
                             password='1031125051',
                             database='test',
                             charset='utf8',
                             #muestra los datos como diccionario en vez de tupla
                             #cursorclass=pymysql.cursors.DictCursor
                           )
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'DELETE from persona where id_persona IN %s'
            entrada = input('proporciona los idpersona a eliminar separados por coma: ')
            valores = (tuple(entrada.split(',')),)
            cursor.execute(sentencia, valores)
            conexion.commit()
            registros_eliminados = cursor.rowcount
            print(f'Registros Eliminados: {registros_eliminados}')
except Exception as e:
    print(f'Ocurrio un error: {e}')
# finally:
#     conexion.close()
