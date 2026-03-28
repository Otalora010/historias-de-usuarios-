# ------------------ MANEJO DE ARCHIVOS CSV ------------------

def guardar_csv(inventario, ruta, incluir_header=True):
    """
    Guarda el inventario en un archivo CSV.
    """
    if not inventario:
        print("Inventario vacío. No se puede guardar.\n")
        return

    try:
        with open(ruta, "w", encoding="utf-8") as archivo:

            if incluir_header:
                archivo.write("nombre,precio,cantidad\n")

            for p in inventario:
                archivo.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")

        print(f"Inventario guardado en: {ruta}\n")

    except Exception as e:
        print(f"Error al guardar archivo: {e}\n")


def cargar_csv(ruta):
    """
    Carga un archivo CSV y devuelve una lista de productos.
    """
    inventario = []
    errores = 0

    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()

            if not lineas:
                print("Archivo vacío.\n")
                return []

            header = lineas[0].strip()
            if header != "nombre,precio,cantidad":
                print("Encabezado inválido.\n")
                return []

            for linea in lineas[1:]:
                partes = linea.strip().split(",")

                if len(partes) != 3:
                    errores += 1
                    continue

                nombre, precio, cantidad = partes

                try:
                    precio = float(precio)
                    cantidad = int(cantidad)

                    if precio < 0 or cantidad < 0:
                        errores += 1
                        continue

                    inventario.append({
                        "nombre": nombre,
                        "precio": precio,
                        "cantidad": cantidad
                    })

                except ValueError:
                    errores += 1

        print(f"Archivo cargado. Filas inválidas: {errores}\n")
        return inventario

    except FileNotFoundError:
        print("Archivo no encontrado.\n")
    except UnicodeDecodeError:
        print("Error de codificación.\n")
    except Exception as e:
        print(f"Error inesperado: {e}\n")

    return []