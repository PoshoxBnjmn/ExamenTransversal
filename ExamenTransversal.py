productos = {
    '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
    'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
    '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}

stock = {
    '8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
    'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
    'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0],
}

def busquedaStockMarca():
    guardado = []
    totalStock = 0
    busqueda = ""
    existe = False
    while busqueda == "":
        busqueda = input("\nIngrese marca a consultar: ")
    for datos in productos.items():
        marca = datos[1][0]
        if busqueda.lower() == marca.lower():
            guardado.append(datos[0])
            existe = True
    if existe:
        for clave in stock:
            for datos in guardado:
                if datos == clave:
                    totalStock += stock[clave][1]
                    break
        print(f"\nEl stock es: {totalStock}")
    elif not existe:
        print(f"\nEsta marca no se encuentra disponible\n")

op = 0
while op != 4:
    op = 0
    while op < 1 or op > 4:
        try:
            op = int(input("\n*** MENU PRINCIPAL ***\n1. Stock marca.\n2. Búsqueda por precio.\n3. Actualizar precio.\n4. Salir.\n\n ingrese una opcion: "))
            if op < 1 or op > 4:
                print("\ningrese una opcion valida (1-4)\n")
        except:
            print("\nIngrese una opcion valida (1-4)\n")
    match op:
        case 1:
            busquedaStockMarca()
        case 2:
            print("\nno se puso, ando malito")
        case 3:
            print("\nno se puso, ando malito")
print("Programa finalizado...")