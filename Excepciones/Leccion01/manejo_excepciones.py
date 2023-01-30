from NumerosIdenticosException import NumerosIdenticosException

resultado = None

try:
    a = int(input('Primer Numero: '))
    b = int(input('Segundo Numero: '))
    if a == b:
        raise NumerosIdenticosException('Numeros Identicos')
    resultado = a/b
except ZeroDivisionError as e:
    print(f'Ocurrio un error: {e}')
except TypeError as e:
    print(f'Ocurrio un error: {e}')
except Exception as e:
    print(f'Ocurrio un error: {e}')
else:
    print('No se arrojo ninguna excepcion')
finally:
    print('Elegante como el pegante')

print(f'Resultado: {resultado}')
print('Continuamos...')