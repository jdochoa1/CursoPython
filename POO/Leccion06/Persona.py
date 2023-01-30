class Persona:
    contador_personas = 0

    @classmethod
    def generar_siguiente_valor(cls):
        cls.contador_personas += 1
        return cls.contador_personas

    def __init__(self, nombre, edad):
        self. id_persona = Persona.generar_siguiente_valor()
        self.nombre = nombre
        self.edad =edad

    def __str__(self):
        return f'Persona [{self.id_persona} {self.nombre} {self.edad}]'

persona1 = Persona('Juan', 21)
print(persona1)

persona2 = Persona('Karla', 30)
print(persona2)

persona3 = Persona('Eduardo', 50)
print(persona3)

Persona.generar_siguiente_valor()

print(f'Valor contador persona: {Persona.contador_personas}')