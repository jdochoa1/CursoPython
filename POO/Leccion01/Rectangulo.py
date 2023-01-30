class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcularArea(self):
        return self.base * self.altura

base = int(input('Proporcione la base: '))
altura = int(input('Proporcione la altura: '))
rectangulo1 = Rectangulo(base,altura)
print(f'El area es: {rectangulo1.calcularArea()}')