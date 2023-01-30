import math
from decimal import Decimal
# NaN - Not a numer (no es un numero)
# NaN no es sensible a mayusculas o minusculas
# NaN es un tipo de dato numerico para representar un valor indefinido
a = float('NaN')
# print(f'a: {a}')
# print(f'Es NaN (not a number)? {math.isnan(a)}')

a = Decimal('NaN')
print(f'a: {a}')
print(f'Es NaN (not a number)? {math.isnan(a)}')
