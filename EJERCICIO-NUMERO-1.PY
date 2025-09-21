print ("Escribir un programa que pregunte el nombre del usuario y un número entero e imprima en líneas distintas el nombre del usuario tantas veces como el número introducido")
print ("----------------------------------------------------------------")
nombre = input("Escriba su nombre: ")
if not nombre:
    print("No ha introducido ningún nombre")
    exit()
veces = int(input("Escriba la cantidad de veces que quiere que se repita su nombre: " ))
for i in range(veces):
    print (nombre)