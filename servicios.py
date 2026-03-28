# ------------------ SERVICIOS DEL INVENTARIO ------------------

def agregar_producto(inventario, nombre, precio, cantidad):
    """
    Agrega un nuevo producto al inventario.

    Parámetros:
    inventario (list): Lista de productos
    nombre (str): Nombre del producto
    precio (float): Precio del producto
    cantidad (int): Cantidad del producto

    Retorna:
    None
    """
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }
    inventario.append(producto)


def mostrar_inventario(inventario):
    """
    Muestra todos los productos del inventario.
    """
    if not inventario:
        print("El inventario está vacío.\n")
        return

    print("\n--- INVENTARIO ---")
    for p in inventario:
        print(f"Producto: {p['nombre']} | Precio: {p['precio']} | Cantidad: {p['cantidad']}")
    print()


def buscar_producto(inventario, nombre):
    """
    Busca un producto por nombre.

    Retorna:
    dict o None
    """
    for p in inventario:
        if p["nombre"].lower() == nombre.lower():
            return p
    return None


def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    """
    Actualiza precio y/o cantidad de un producto.
    """
    producto = buscar_producto(inventario, nombre)

    if producto is None:
        return False

    if nuevo_precio is not None:
        producto["precio"] = nuevo_precio

    if nueva_cantidad is not None:
        producto["cantidad"] = nueva_cantidad

    return True


def eliminar_producto(inventario, nombre):
    """
    Elimina un producto del inventario.
    """
    producto = buscar_producto(inventario, nombre)

    if producto:
        inventario.remove(producto)
        return True
    return False


def calcular_estadisticas(inventario):
    """
    Calcula estadísticas del inventario.

    Retorna:
    dict con métricas
    """

    if not inventario:
        return None

    unidades_totales = 0
    valor_total = 0

    subtotal = lambda p: p["precio"] * p["cantidad"]

    producto_mas_caro = max(inventario, key=lambda p: p["precio"])
    producto_mayor_stock = max(inventario, key=lambda p: p["cantidad"])

    for p in inventario:
        unidades_totales += p["cantidad"]
        valor_total += subtotal(p)

    return {
        "unidades_totales": unidades_totales,
        "valor_total": valor_total,
        "producto_mas_caro": (producto_mas_caro["nombre"], producto_mas_caro["precio"]),
        "producto_mayor_stock": (producto_mayor_stock["nombre"], producto_mayor_stock["cantidad"])
    }