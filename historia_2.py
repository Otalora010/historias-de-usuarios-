# Inventario simple con menú interactivo (sin usar while True)
# Objetivo: practicar estructura de datos, condicionales, bucles y modularización.

# Función: imprime el menú y devuelve la opción elegida por el usuario
def imprimir_menu():
    print("\n--- Menú de Inventario ---")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Calcular estadísticas")
    print("4. Salir")
    opcion = input("Selecciona una opción (1-4): ").strip()
    return opcion

# Función: agregar un nuevo producto al inventario
def agregar_producto(inventario):
    print("\n-> Agregar producto")
    nombre = input("Nombre del producto: ").strip()
    if not nombre:
        print("Nombre inválido. Intente de nuevo.")
        return

    # Validación de precio
    precio = None
    valido = False
    while not valido:
        precio_input = input("Precio (entero): ").strip()
        try:
            precio = int(precio_input)
            if precio < 0:
                print("Precio debe ser no negativo.")
            else:
                valido = True
        except ValueError:
            print("Precio inválido. Debe ser un número entero.")

    # Validación de cantidad
    cantidad = None
    valido = False
    while not valido:
        cantidad_input = input("Cantidad: ").strip()
        try:
            cantidad = int(cantidad_input)
            if cantidad < 0:
                print("Cantidad debe ser no negativa.")
            else:
                valido = True
        except ValueError:
            print("Cantidad inválida. Debe ser un número entero.")

    producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
    inventario.append(producto)
    print(f"Producto agregado: {nombre}")

# Función: mostrar todos los productos del inventario
def mostrar_inventario(inventario):
    print("\n-> Inventario")
    if not inventario:
        print("El inventario está vacío.")
    else:
        for p in inventario:
            print(f"Producto: {p['nombre']} | Precio: {p['precio']} | Cantidad: {p['cantidad']}")

# Función: calcular estadísticas básicas
def calcular_estadisticas(inventario):
    print("\n-> Estadísticas")
    if not inventario:
        print("No hay productos en el inventario.")
        return
    valor_total = sum(p['precio'] * p['cantidad'] for p in inventario)
    total_productos = sum(p['cantidad'] for p in inventario)
    print(f"Valor total del inventario: {valor_total}")
    print(f"Número total de productos registrados (unidades): {total_productos}")

# Punto de entrada
if __name__ == "__main__":
    inventario = []  # lista de diccionarios: [{"nombre": ..., "precio": ..., "cantidad": ...}, ...]

    opcion = ""
    # Bucle principal: se mantiene activo hasta que el usuario elige salir (opción "4")
    while opcion != "4":
        opcion = imprimir_menu()
        if opcion == "1":
            agregar_producto(inventario)
        elif opcion == "2":
            mostrar_inventario(inventario)
        elif opcion == "3":
            calcular_estadisticas(inventario)
        elif opcion == "4":
            print("Saliendo del programa. ¡Hasta luego!")
        else:
            # Manejo de opciones inválidas sin cerrar el programa
            print("Opción inválida. Por favor, elige una opción entre 1 y 4.")

    # Resumen final (comentario final resumido)
    # Objetivo de la semana: crear un módulo de inventario básico con entrada de usuario,
    # almacenamiento en lista de diccionarios, operaciones de visualización y estadísticas,
    # y una estructura de código legible y modular.