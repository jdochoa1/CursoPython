class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return f'Vehiculo: {self.color} {self.ruedas}'

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return f'Coche:{self.velocidad}km/h {super().__str__()}'

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return f'Bicicleta: {self.tipo} {super().__str__()} '

vehiculo1 = Vehiculo('Rojo', 4)
print(vehiculo1)

coche1 = Coche('Azul',4,200)
print(coche1)

bicicleta1 = Bicicleta('Amarilla',2,'Ruta')
print(bicicleta1)

