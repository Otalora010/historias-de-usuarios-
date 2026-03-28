from servicios import *
from archivos import *


# Inventario en memoria
inventario = []


def menu():
    opcion = ""

    while opcion != "9":
        print("=== MENÚ ===")
        print("1. Agregar")
        print("2. Mostrar")
        print("3. Buscar")
        print("4. Actualizar")
        print("5. Eliminar")
        print("6. Estadísticas")
        print("7. Guardar CSV")
        print("8. Cargar CSV")
        print("9. Salir")

        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                nombre = input("Nombre: ")
                precio = float(input("Precio: "))
                cantidad = int(input("Cantidad: "))
                agregar_producto(inventario, nombre, precio, cantidad)

            elif opcion == "2":
                mostrar_inventario(inventario)

            elif opcion == "3":
                nombre = input("Nombre a buscar: ")
                p = buscar_producto(inventario, nombre)
                print(p if p else "No encontrado\n")

            elif opcion == "4":
                nombre = input("Producto a actualizar: ")
                precio = input("Nuevo precio (enter para omitir): ")
                cantidad = input("Nueva cantidad (enter para omitir): ")

                precio = float(precio) if precio else None
                cantidad = int(cantidad) if cantidad else None

                if actualizar_producto(inventario, nombre, precio, cantidad):
                    print("Actualizado\n")
                else:
                    print("No encontrado\n")

            elif opcion == "5":
                nombre = input("Producto a eliminar: ")
                if eliminar_producto(inventario, nombre):
                    print("Eliminado\n")
                else:
                    print("No encontrado\n")

            elif opcion == "6":
                stats = calcular_estadisticas(inventario)
                if stats:
                    print(stats, "\n")
                else:
                    print("Inventario vacío\n")

            elif opcion == "7":
                ruta = input("Ruta del archivo: ")
                guardar_csv(inventario, ruta)

            elif opcion == "8":
                ruta = input("Ruta del archivo: ")
                nuevos = cargar_csv(ruta)

                if nuevos:
                    opcion_merge = input("¿Sobrescribir? (S/N): ").lower()

                    if opcion_merge == "s":
                        inventario.clear()
                        inventario.extend(nuevos)
                    else:
                        for nuevo in nuevos:
                            existente = buscar_producto(inventario, nuevo["nombre"])
                            if existente:
                                existente["cantidad"] += nuevo["cantidad"]
                                existente["precio"] = nuevo["precio"]
                            else:
                                inventario.append(nuevo)

            elif opcion == "9":
                print("Saliendo...")

            else:
                print("Opción inválida\n")

        except Exception as e:
            print(f"Error: {e}\n")


menu()