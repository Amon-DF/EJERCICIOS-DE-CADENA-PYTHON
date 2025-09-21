print("Escribir un programa que pregunte por los productos de una cesta de compras, separados por comas, y muestre cada uno de los productos en una línea distinta")
print ("----------------------------------------------------------------")
productos = input("Escriba los productos de su cesta de compras, separados por comas: ")
if not productos:
    print("No ha introducido ningún producto")
    exit()
lista_productos = productos.split(",")
print("Los productos de su cesta de compras son: ")
for producto in lista_productos:
    print("- " + producto.strip().capitalize())