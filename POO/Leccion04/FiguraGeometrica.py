#ABC Abstract Base Class
from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
    def __init__(self, ancho, alto):
        if self._validar_valor(ancho):
            self._ancho = ancho
        else:
            self._ancho = 0
            print(f'Valor Erroneo:{ancho}')
        if self._validar_valor(alto):
            self._alto = alto
        else:
            self._alto = 0
            print(f'Valor Erroneo:{alto}')

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, ancho):
        if self._validar_valor(ancho):
            self._ancho = ancho
        else:
            print(f'Valor Erroneo:{ancho}')

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, alto):
        if self._validar_valor(alto):
            self._alto = alto
        else:
            print(f'Valor Erroneo:{alto}')

    @abstractmethod
    def calcularArea(self):
        pass

    def __str__(self):
        return f'Figura geometrica [Ancho:{self._ancho} Alto: {self._alto}]'

    def _validar_valor(self, valor):
        return True if 0 < valor < 10 else False
