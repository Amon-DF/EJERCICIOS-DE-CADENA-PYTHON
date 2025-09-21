print("Escribir un programa que pregunte el nombre de un producto, su precio y un número de unidades y muestre una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales")
print ("----------------------------------------------------------------")
nombre_producto = input("Escriba el nombre del producto: ")
if not nombre_producto:
    print("No ha introducido ningún nombre de producto")
    exit()
precio_producto = float(input("Escriba el precio del producto (con dos decimales, en dólares): "))
numero_unidades = int(input("Escriba el número de unidades: "))
coste_total = precio_producto * numero_unidades
print(f"Producto: {nombre_producto}, Precio unitario: ${precio_producto:09.2f}, Unidades: {numero_unidades:03d}, Coste total: ${coste_total:011.2f}")