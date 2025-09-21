print("Escribir un programa que pregunte el nombre del usuario y después de que el usuario lo introduzca muestre: *<nombre> tiene <n> letras*, donde <nombre> es el nombre de usuario en mayúsculas y <n> es el número de letras que tiene el nombre")
print ("----------------------------------------------------------------")
nombre = input("Escriba su nombre: ")
if not nombre:
    print("No ha introducido ningún nombre")
    exit()
nombre_sin_espacios = nombre.replace(" ", "")
print("El nombre", nombre.upper() + " tiene " + str(len(nombre_sin_espacios)) + " letras")