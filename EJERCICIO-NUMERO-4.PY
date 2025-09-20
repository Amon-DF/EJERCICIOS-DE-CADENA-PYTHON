print("Los teléfonos de una empresa tienen el siguiente formato: <prefijo-número-extensión> donde el prefijo es *+34*, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un programa que pregunte por un número de teléfono con este formato y muestre el número de teléfono sin el prefijo y la extensión")
print ("--------------------------------------------------------------")
print("Escriba su número de teléfono con el formato <PREFIJO (+34) - NÚMERO - EXTENSIÓN (2 dígitos)>: ")
print("(Por ejemplo: +34-913724710-56)")
telefono = input()
if not telefono:
    print("No ha introducido ningún número de teléfono")
    exit()
numero_sin_prefijo_y_extension = telefono[4:-3]
print("El número de teléfono sin el prefijo y la extensión es: " + numero_sin_prefijo_y_extension)