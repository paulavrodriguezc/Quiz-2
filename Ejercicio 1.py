#======================================
#Nombre del estudiante: Paula Rodríguez
#Carnet: 20221110264
#======================================
from Electrodomestico import Electrodomestico, Lavadora, Microondas, Nevera, Licuadora
def greet_and_menu():
    option=input("¡Bienvenido al sistema de Ventas Naranja! \nSeleccione una opción dentro de las dadas: \n1. Leer inventario \n2. Eliminar producto defectuoso \n3. Salir del sistema \n---> ")
    while not option.isnumeric() or not option in ["1", "2", "3"]:
       option=input("Opción inválida. \nSeleccione una opción dentro de las dadas: \n1. Leer inventario \n2. Eliminar producto defectuoso \n3. Salir del sistema \n---> ")
    return int(option)
def read_edd(edd: dict, products_updated: list, products_codes: list):
    for type_product, products in edd.items():
        if type_product=="washer":
            for product in products:
                washer=Lavadora(product["cod_p"],product["price"],product["brand"],product["color"],product["capacity"])
                products_updated.append(washer)
                products_codes.append(product["cod_p"])
        elif type_product=="microwave":
            for product in products:
                microwave=Microondas(product["cod_p"],product["price"],product["brand"],product["color"],product["digital"])
                products_updated.append(microwave)
                products_codes.append(product["cod_p"])
        elif type_product=="fridge":
            for product in products:
                fridge=Nevera(product["cod_p"],product["price"],product["brand"],product["color"],product["cooler"],product["comp"])
                products_updated.append(fridge)
                products_codes.append(product["cod_p"])
        else:
            for product in products:
                blender=Licuadora(product["cod_p"],product["price"],product["brand"],product["color"],product["cup"],product["speeds"])
                products_updated.append(blender)
                products_codes.append(product["cod_p"])
def print_products_available(products_updated: list):
    for product in products_updated:
        product.mostrar()
def delete_product(products_updated: list, products_codes: list, products_deleted: list):
    keep=True
    while keep:
        product_deleted=input("Por favor, introduzca el código del producto defectuoso: ")
        while not product_deleted in products_codes:
            product_deleted=input("Producto no disponible. Por favor, introduzca el código del producto defectuoso: ")
        for product in products_updated:
            if product.codigo_producto==product_deleted:
                products_deleted.append(product)
                products_updated.remove(product)
        option_given=input("¿Desea continuar? \n1. Sí \n2. No \n---> ")
        while not option_given.isnumeric() or not option_given in ["1","2"]:
            option_given=input("Opción inválida. ¿Desea continuar? \n1. for sí \n2. for no \n---> ")
        if option_given=="2":
            keep=False
def print_fridge(products_updated: list):
    for product in products_updated:
        try:
            if product.inc_congelador:
                print(f"La nevera de código {product.codigo_producto}: ")
                print(f"\t Tiene congelador: {product.inc_congelador}")
        except:
            pass
def main():
    continuing=True
    products_updated=[]
    products_codes=[]
    products_deleted=[]
    edd = {
    "washer":
    [
        {"cod_p": "AEX-200918", "price": 551.99, "brand": "Whirlpool", "color": "Blanca", "capacity": 17},
        {"cod_p": "GHT-191214", "price": 409.00, "brand": "LG", "color": "Gris", "capacity": 15}
    ],
    "microwave":
    [
        {"cod_p": "FGE-220708", "price": 109.01, "brand": "Daewoo", "color": "Blanco", "digital": False},
        {"cod_p": "PEP-210123", "price": 201.50, "brand": "Frigilux", "color": "Negro", "digital": True}
    ],
    "fridge":
    [
        {"cod_p": "HYW-180909", "price": 280.98, "brand": "Electrolux", "color": "Plateado", "cooler": False, "comp": 5},
        {"cod_p": "IUO-201020", "price": 405.99, "brand": "Samsung", "color": "Azul pastel y rosado", "cooler": True, "comp": 8}
    ],
    "blender":
    [
        {"cod_p": "OWO-191111", "price": 42.05, "brand": "Oster", "color": "Plateado", "cup": "Cristal", "speeds": 3},
        {"cod_p": "XAT-221230", "price": 17.99, "brand": "Philips", "color": "Blanco", "cup": "Plastico", "speeds": 2}
    ]
}
    while continuing:
        option=greet_and_menu()
        if option==1:
            read_edd(edd, products_updated, products_codes)
            print_products_available(products_updated)
            fridges_available=input("¿Desea SÓLO ver las neveras disponibles y si tienen congelador? \n1. Sí \n2. No \n---> ")
            while not fridges_available.isnumeric() or not fridges_available in ["1","2"]:
                fridges_available=input("Opción inválida. ¿Desea SÓLO ver las neveras disponibles y si tienen congelador? \n1. Sí \n2. No \n---> ")
            if fridges_available=="1":
                print_fridge(products_updated)
        elif option==2:
            option_2=input("Por favor seleccione qué desea hacer: \n1. Eliminar producto defectuoso \n2. Mostrar productos defectuosos \n---> ")
            while not option_2.isnumeric() or not option_2 in ["1", "2"]:
                option_2=input("Opción inválida. Por favor seleccione qué desea hacer: \n1. Eliminar producto defectuoso \n2. Mostrar productos defectuosos \n---> ")
            if option_2=="1":
                print_products_available(products_updated)
                delete_product(products_updated, products_codes, products_deleted)
                print(products_deleted)
            else:
                print_products_available(products_deleted)
        else:
            print("¡Gracias por preferirnos! Feliz día.")
            continuing=False
main()