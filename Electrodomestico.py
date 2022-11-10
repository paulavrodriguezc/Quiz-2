class Electrodomestico:
    def __init__(self, codigo_producto, precio, marca, color):
        self.codigo_producto=codigo_producto
        self.precio=precio
        self.marca=marca
        self.color=color
    def mostrar(self):
        print(f"*Código producto: {self.codigo_producto} \n*Precio: {self.precio} \n*Marca: {self.marca} \n*Color: {self.color}\n")
class Lavadora(Electrodomestico):
    def __init__(self, codigo_producto, precio, marca, color, capacidad):
        super().__init__(codigo_producto, precio, marca, color)
        self.capacidad=capacidad
    def mostrar(self):
        print(f"*Código producto: {self.codigo_producto} \n*Precio: {self.precio} \n*Marca: {self.marca} \n*Color: {self.color} \n*Capacidad: {self.capacidad} \n")
class Microondas(Electrodomestico):
    def __init__(self, codigo_producto, precio, marca, color, control):
        super().__init__(codigo_producto, precio, marca, color)
        self.control=control
    def mostrar(self):
        print(f"*Código producto: {self.codigo_producto} \n*Precio: {self.precio} \n*Marca: {self.marca} \n*Color: {self.color} \n*Tiene control digital: {self.control} \n")
class Nevera(Electrodomestico):
    def __init__(self, codigo_producto, precio, marca, color, inc_congelador, compartimientos):
        super().__init__(codigo_producto, precio, marca, color)
        self.inc_congelador=inc_congelador
        self.compartimientos=compartimientos
    def mostrar(self):
        print(f"*Código producto: {self.codigo_producto} \n*Precio: {self.precio} \n*Marca: {self.marca} \n*Color: {self.color} \n*Incluye congelador: {self.inc_congelador} \n*Compartimientos: {self.compartimientos}\n")
class Licuadora(Electrodomestico):
    def __init__(self, codigo_producto, precio, marca, color, material_vaso, velocidades):
        super().__init__(codigo_producto, precio, marca, color)
        self.material_vaso=material_vaso
        self.velocidades=velocidades
    def mostrar(self):
        print(f"*Código producto: {self.codigo_producto} \n*Precio: {self.precio} \n*Marca: {self.marca} \n*Color: {self.color} \n*Material del vaso: {self.material_vaso} \n*Velocidades: {self.velocidades}\n")