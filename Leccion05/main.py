# dict (key , value)
diccionario = {
    'IDE':'Integrated Development Environment',
    'OOP':'Object Oriented Programming',
    'DBMS':'Database Management System'
}
print(diccionario)
#largo
print(len(diccionario))
# acceder a un elemento (key)
print(diccionario['IDE'])
# otra forma de recuperar un elemento
print(diccionario.get('OOP'))
# modificando elementos
diccionario['IDE'] = 'Chiche y las bolas'
print(diccionario)
# recorrer los elementos
for termino, valor in diccionario.items():
    print(termino, valor)

for termino in diccionario.keys():
    print(termino)

for valor in diccionario.values():
    print(valor)

# comprobar la existencia de un elemento
print('IDE' in diccionario)

#agrehar un elemento
diccionario['PK'] = 'Primary Key'
print(diccionario)

#remover un elemento
diccionario.pop('DBMS')
print(diccionario)

#limpiar el diccionario
diccionario.clear()
print(diccionario)

#eliminar el diccionario
del diccionario