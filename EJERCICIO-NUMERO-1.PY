print ("Escribir un programa que pregunte el nombre del usuario y un número entero e imprima en líneas distintas el nombre del usuario tantas veces como el número introducido")
print ("--------------------------------------------------------------")
print ("Escriba su nombre: ")
nombre = input()
if not nombre:
    print("No ha introducido ningún nombre")
    exit()
print ("Escriba la cantidad de veces que quiere que se repita su nombre: ")
veces = int(input())
for i in range(veces):
    print (nombre)