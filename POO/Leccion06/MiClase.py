class MiClase:

    variableClase = 'Valor variable clase'

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia

    @staticmethod
    def metodo_estatico():
        print(MiClase.variableClase)

    @classmethod
    def metodo_clase(cls):
        print(cls.variableClase)

    def metodo_instancia(self):
        self.metodo_clase()
        self.metodo_estatico()

print(MiClase.variableClase)
miClase = MiClase('Valor variable instancia')
# print(miClase.variableClase)
# print(miClase.variable_instancia)




miClase2 = MiClase("Otro valor de instancia")
# print(miClase2.variableClase)
# print(miClase2.variable_instancia)
# print(MiClase.variableClase2)
# print(miClase.variableClase2)
# print(miClase.variableClase2)


objeto1 = MiClase('Valor variable clase 2')
objeto1.metodo_instancia()
MiClase.metodo_estatico()
MiClase.metodo_clase()
objeto1.metodo_instancia()