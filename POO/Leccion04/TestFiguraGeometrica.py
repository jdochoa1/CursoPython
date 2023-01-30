from Cuadrado import Cuadrado
from FiguraGeometrica import FiguraGeometrica
from Rectangulo import Rectangulo

#No se puede instanciar una clase abstracta
#figura = FiguraGeometrica()

print('Creacion de cuadrado'.center(50,'-'))
cuadrado1 = Cuadrado(lado=5, color='rojo')
print(cuadrado1.calcularArea())
print(cuadrado1)

print('Creacion de rectangulo'.center(50,'-'))
rectangulo1 = Rectangulo(ancho=3, alto=8, color='verde')
rectangulo1.ancho = 15
print(rectangulo1.calcularArea())
print(rectangulo1)
