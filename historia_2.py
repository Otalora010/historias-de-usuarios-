# ------------------ INVENTARIO ------------------

# Lista global donde se guardarán los productos
inventario = []


# ------------------ FUNCIÓN: AGREGAR PRODUCTO ------------------
def agregar_producto():
    """
    Solicita al usuario los datos de un producto (nombre, precio y cantidad)
    y lo agrega al inventario como un diccionario.
    """

    nombre = input("Ingrese el nombre del producto: ")

    # Validación del precio
    precio_valido = False
    while not precio_valido:
        precio = input("Ingrese el precio del producto: ")

        if precio.replace('.', '', 1).isdigit():
            precio = float(precio)
            if precio > 0:
                precio_valido = True
            else:
                print("El precio debe ser mayor a 0.")
        else:
            print("Ingrese un número válido.")

    # Validación de la cantidad
    cantidad_valida = False
    while not cantidad_valida:
        cantidad = input("Ingrese la cantidad del producto: ")

        if cantidad.isdigit():
            cantidad = int(cantidad)
            if cantidad > 0:
                cantidad_valida = True
            else:
                print("La cantidad debe ser mayor a 0.")
        else:
            print("Ingrese un número entero válido.")

    # Crear el producto como diccionario
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    # Agregar al inventario
    inventario.append(producto)

    print("Producto agregado correctamente.\n")


# ------------------ FUNCIÓN: MOSTRAR INVENTARIO ------------------
def mostrar_inventario():
    """
    Recorre el inventario y muestra todos los productos.
    Si está vacío, muestra un mensaje.
    """

    if len(inventario) == 0:
        print("El inventario está vacío.\n")
    else:
        print("\n--- INVENTARIO ---")
        for producto in inventario:
            print(f"Producto: {producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}")
        print()


# ------------------ FUNCIÓN: CALCULAR ESTADÍSTICAS ------------------
def calcular_estadisticas():
    """
    Calcula:
    - Valor total del inventario (precio * cantidad)
    - Cantidad total de productos
    """

    if len(inventario) == 0:
        print("No hay productos para calcular estadísticas.\n")
        return

    valor_total = 0
    total_productos = 0

    # Recorrer inventario
    for producto in inventario:
        valor_total += producto["precio"] * producto["cantidad"]
        total_productos += producto["cantidad"]

    print("\n--- ESTADÍSTICAS ---")
    print(f"Valor total del inventario: {valor_total}")
    print(f"Cantidad total de productos: {total_productos}\n")


# ------------------ FUNCIÓN: MENÚ PRINCIPAL ------------------
def menu():
    """
    Muestra el menú principal y controla el flujo del programa.
    Se ejecuta hasta que el usuario decide salir.
    """

    opcion = ""

    # Bucle controlado (NO while True)
    while opcion != "4":
        print("=== MENÚ INVENTARIO ===")
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Calcular estadísticas")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            mostrar_inventario()
        elif opcion == "3":
            calcular_estadisticas()
        elif opcion == "4":
            print("Saliendo del sistema...")
        else:
            print("Opción inválida. Intente nuevamente.\n")


# ------------------ EJECUCIÓN DEL PROGRAMA ------------------
menu()


# ------------------ COMENTARIO FINAL ------------------
"""
Este programa permite gestionar un inventario
Se aplicaron estructuras como condicionales, bucles, listas y diccionarios,
además de modularización mediante funciones.

El sistema permite:
- Agregar productos con validación de datos
- Mostrar el inventario completo
- Calcular estadísticas básicas

El objetivo es practicar lógica de programación y organización del código.
"""