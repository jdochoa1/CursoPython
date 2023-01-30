class Cubo:
    def __init__(self, ancho, alto, profundo):
        self.ancho = ancho
        self.alto = alto
        self.profundo = profundo

    def calcularVolumen(self):
        return self.ancho * self.alto * self.profundo

ancho = int(input('Proporcione el ancho: '))
alto = int(input('Proporcione el alto: '))
profundo = int(input('Proporcione la profundidad: '))

cubo1 = Cubo(ancho,alto,profundo)
print(f'El volumen es: {cubo1.calcularVolumen()}')
