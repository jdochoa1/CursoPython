# Leer archivo json
# json = JavaScript Object Notation
import urllib.request
import json

respuesta = urllib.request.urlopen('http://globalmentoring.com.mx/api/personas.json')
print(respuesta)
cuerpo_respuesta = respuesta.read()
print(cuerpo_respuesta)
# Procesamos la respuesta json
json_respuesta = json.loads(cuerpo_respuesta.decode("utf-8"))
print(json_respuesta)
# Imprimimos sólo los nombres de las personas
# json se convierte a listas y diccionarios de python
print('Nombres de las personas en el archivo json:')
for persona in json_respuesta['personas']:
    print(persona['nombre'], persona['edad'])
# Accedemos al total de personas de archivo
print(f'Total de personas: {json_respuesta["total"]}')
# Accedemos al mensaje del archivo
print(f'Mensaje: {json_respuesta["mensaje"]}')
