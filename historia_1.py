# --------------------------------------------------
# Función para validar si un valor es un número decimal positivo
# --------------------------------------------------
def es_numero_valido(valor):
    # Se elimina un punto (.) para permitir números decimales
    # y luego se verifica si el resto son dígitos
    return valor.replace('.', '', 1).isdigit()


# --------------------------------------------------
# Función para solicitar y validar los datos del producto
# --------------------------------------------------
def obtener_datos_producto():
    
    # Solicitar el nombre del producto (string)
    nombre = input("Agregue el nombre del producto: ")
    
    # ------------------ VALIDACIÓN DEL PRECIO ------------------
    # Inicializamos el precio con un valor inválido
    precio = -1
    
    # Se repite hasta que el usuario ingrese un valor válido mayor a 0
    while precio <= 0:
        entrada = input("Agregue el costo del producto: ")
        
        # Verificamos si el valor ingresado es un número válido
        if es_numero_valido(entrada):
            precio = float(entrada)  # Convertimos a número decimal
            
            # Validamos que sea mayor a 0
            if precio <= 0:
                print("Error: El costo debe ser mayor a 0.")
        else:
            print("Error: Ingrese un número válido.")
    
    # ------------------ VALIDACIÓN DE LA CANTIDAD ------------------
    # Inicializamos la cantidad con un valor inválido
    cantidad = -1
    
    # Se repite hasta que el usuario ingrese un entero válido mayor a 0
    while cantidad <= 0:
        entrada = input("Agregue la cantidad del producto: ")
        
        # Verificamos que sea un número entero
        if entrada.isdigit():
            cantidad = int(entrada)  # Convertimos a entero
            
            # Validamos que sea mayor a 0
            if cantidad <= 0:
                print("Error: La cantidad debe ser mayor a 0.")
        else:
            print("Error: Ingrese un número entero válido.")
    
    # Retornamos los datos validados
    return nombre, precio, cantidad


# --------------------------------------------------
# Función para calcular el costo total del producto
# --------------------------------------------------
def calcular_costo_total(precio, cantidad):
    # Multiplicamos el precio por la cantidad
    return precio * cantidad


# --------------------------------------------------
# Función para mostrar los resultados en consola
# --------------------------------------------------
def mostrar_resultados(nombre, precio, cantidad, costo_total):
    
    # Mostrar encabezado tipo factura
    print("\n" + "="*50)
    print("           Factura de Compra - Tiendas el cachaco           ")
    print("="*50)
    
    # Mostrar información detallada del producto
    print(f"Producto: {nombre}")
    print(f"Precio unitario: ${precio:.2f} COP")
    print(f"Cantidad: {cantidad}")
    print(f"Costo total: ${costo_total:.2f} COP")
    
    print("="*50)
    
    # Mostrar formato compacto solicitado
    print(f"Formato compacto: {nombre} | ${precio:.2f} COP | {cantidad} | ${costo_total:.2f} COP")


# --------------------------------------------------
# Función principal del programa
# --------------------------------------------------
def main():
    
    # Mensaje de bienvenida
    print("=== Bienvenidos a Tiendas el cachaco ===")
    print("Registro de productos en inventario\n")
    
    # Solicitar datos del producto
    nombre, precio, cantidad = obtener_datos_producto()
    
    # Calcular el costo total
    costo_total = calcular_costo_total(precio, cantidad)
    
    # Mostrar los resultados en pantalla
    mostrar_resultados(nombre, precio, cantidad, costo_total)


# --------------------------------------------------
# Punto de entrada del programa
# --------------------------------------------------
if __name__ == "__main__":
    main()


# --------------------------------------------------
# DESCRIPCIÓN GENERAL DEL PROGRAMA
# --------------------------------------------------
# Este programa permite registrar un producto en un sistema de inventario.
# Solicita al usuario el nombre, precio y cantidad del producto, validando
# que el precio sea un número decimal positivo y que la cantidad sea un
# número entero positivo. Una vez validados los datos, calcula el costo
# total multiplicando el precio por la cantidad. Finalmente, muestra toda
# la información en consola en un formato claro y organizado.