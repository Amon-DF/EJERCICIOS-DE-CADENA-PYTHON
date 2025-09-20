print("Escribir un programa que pregunte el precio de un producto en euros con dos decimales y muestre el número de euros y el número de céntimos del precio introducido")
print("---------------------------------------------------------------")
print("Escriba el precio de un producto (con dos decimales, en euros): ")
precio = input()
if not precio:
    print("No ha introducido ningún precio")
    exit()
euros = precio.split(",") [0]
centimos = precio.split(",") [1]
print("El precio del producto es de " + euros + " euros con " + centimos + " céntimos")