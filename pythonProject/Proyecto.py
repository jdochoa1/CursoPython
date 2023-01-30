listaControl = []
# ,"bomba","pestañina","labial","juguete","florero","aretes","alcancia","maleta","botilo","vaso","cuaderno","herramientas","cremas","tarro"]


class control():
    contador_item = 0
    def __init__(self, _producto, _inventario, _costo, _ventas_octubre, _ventas_noviembre, _ventas_diciembre):
        control.contador_item += 1
        self.item = control.contador_item
        self.producto = _producto
        self.inventario = _inventario
        self.costo = _costo
        self.ventas_octubre = _ventas_octubre
        self.ventas_noviembre = _ventas_noviembre
        self.ventas_diciembre = _ventas_diciembre
        self.ventas_total_trimestre = (_ventas_octubre + _ventas_noviembre + _ventas_diciembre)
        self.productos_registrados = []

    def __str__(self):
         return f'Item: [{self.item}] Nombre: [{self.producto}] Inventario: [{self.inventario}] Ventas Trimestre: [${self.ventas_total_trimestre}]'

    def entregarDatos(self):
        print("item: {} - {} {} - ventas_total_trimestre: {}".format(self.item, self.producto, self.inventario,
                                                                     self.ventas_total_trimestre))

    def editarNotas(self, _ventas_octubre, _ventas_noviembre, _ventas_diciembre):
        self.ventas_octubre = _ventas_octubre
        self.ventas_noviembre = _ventas_noviembre
        self.ventas_diciembre = _ventas_diciembre
        self.ventas_total_trimestre = (_ventas_octubre + _ventas_noviembre + _ventas_diciembre)
        print("Registro Exitoso!")


    def incluirEvento(self, _ventas_octubre,_ventas_noviembre,_ventas_diciembre):
        return ("modificacion: _ventas_octubre: {} _ventas_noviembre: {} _ventas_diciembre: {}".format(_ventas_octubre,
                                                                                               _ventas_noviembre,
                                                                                               _ventas_diciembre))


    def entregaproductos_registrados(self, producto):
        print("No. _item: {} - {} {}".format(producto, self.producto, self.inventario))


def registrarProducto():
    print("Registro de control\n")
    #item = int(input("Ingrese el numero de item: "))
    producto = input("Ingrese el nombre del producto: ")
    inventario = int(input("Ingrese las unidades disponibles de inventario: "))
    costo = int(input("Ingrese el valor acordado: "))
    ventas_octubre = int(input("Ingrese las ventas de octubre: "))
    ventas_noviembre = int(input("Ingrese las ventas de noviembre: "))
    ventas_diciembre = int(input("Ingrese las ventas de diciembre: "))
    objAlumno = control(producto, inventario, costo, ventas_octubre, ventas_noviembre, ventas_diciembre)
    listaControl.append(objAlumno)


def mostrar_producto():
    print("Listado de control\n")
    for objAlumno in listaControl:
        print (objAlumno)


def buscar_producto():
    print("Buscar producto\n")
    item = int(input("Ingrese el numero del item a buscar: "))
    for objAlumno in listaControl:
        if item == objAlumno.item:
            objAlumno.entregarDatos()


def modificarNotas():
    print("Modificar Notas\n")
    item = int(input("Ingrese el numero de item a buscar: "))
    for objAlumno in listaControl:
        if item == objAlumno.item:
            ventas_octubre = float(input("Ingrese las ventas de octubre: "))
            ventas_noviembre = float(input("Ingrese las ventas de noviembre: "))
            ventas_diciembre = float(input("Ingrese las ventas de diciembre: "))
            objAlumno.editarNotas(ventas_octubre, ventas_noviembre, ventas_diciembre)
            objAlumno.entregarDatos()
            recepcionMensaje = objAlumno.incluirEvento(ventas_octubre, ventas_noviembre, ventas_diciembre)
            objAlumno.productos_registrados.append(recepcionMensaje)


def consultarproductos_registrados():
    print("Consulta de productos registrados\n")
    item = int(input("Ingrese el numero de item a buscar: "))
    for objAlumno in listaControl:
        if item == objAlumno.item:
            for recepcionMensaje in objAlumno.productos_registrados:
                print("Evento: {}".format(recepcionMensaje))


def salir():
    print("Salida inminente...!")
    exit()

producto1 = control('Bomba', 500,2000, 150, 200, 100)
listaControl.append(producto1)
producto2 = control('Pestañina', 300,1500, 200, 400, 300)
listaControl.append(producto2)

if __name__ == '__main__':
    opcion = None
    while opcion != 6:
        print("\n")
        print("|****************************|")
        print("|**|      Bienvenidos     |**|")
        print("|**|  Ventas Cacharreria  |**|")
        print("|****************************|")
        print("")
        print("Seleccione una de las siguientes opciones:");
        print("1.- Registrar producto")
        print("2.- Mostrar productos")
        print("3.- Buscar producto por item")
        print("4.- Modificar ventas")
        print("5.- Consultar productos registrados")
        print("6.- Salir\n")
        opcion = int(input("opcion: "))
        if opcion == 1:
            registrarProducto()
        elif opcion == 2:
            mostrar_producto()
        elif opcion == 3:
            buscar_producto()
        elif opcion == 4:
            modificarNotas()
        elif opcion == 5:
            consultarproductos_registrados()
        elif opcion == 6:
            salir()