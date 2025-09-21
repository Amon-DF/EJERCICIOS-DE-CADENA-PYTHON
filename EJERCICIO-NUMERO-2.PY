print("Escribir un programa que pregunte el nombre completo del usuario y después muestre el nombre del usuario tres veces, una con todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúsculas")
print ("----------------------------------------------------------------")
nombre = input("Escriba su nombre: ")
if not nombre:
    print("No ha introducido ningún nombre")
    exit()
print(nombre.lower())
print(nombre.upper())
print(nombre.title())