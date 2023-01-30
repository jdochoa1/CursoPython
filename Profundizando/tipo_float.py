# Profundizando tipo float
a = 3.0
print(f'a: {a:.2f}')
# Constructor float puede recibir int y string
a = float(10)
a = float('10')
print(f'a: {a:.2f}')
# Notacion exponencial (valores positivos o negativos)
a = 3e5
a = 3e-5
print(f'a: {a:.5f}')
# Cualquier calculo que involucre un float, se promueve a float
a = 4.0 + 5
print(f'a: {a:.2f}')
print(type(a))