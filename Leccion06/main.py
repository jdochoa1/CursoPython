def calcular_total(valor, porcentaje):
    impuesto = valor * porcentaje / 100
    total = valor + impuesto
    print(f'El valor a pagar es:{total}')

valor = float(input('Ingrese el valor: '))
porcentaje = float(input('ingrese el porcentaje de impuesto: '))
calcular_total(valor,porcentaje)