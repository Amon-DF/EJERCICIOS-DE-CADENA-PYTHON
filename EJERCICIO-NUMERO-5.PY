print("Escribir un programa que pida al usuario que introduzca una frase y una vocal, y después muestre la misma frase, pero con la vocal introducida en mayúscula")
print ("--------------------------------------------------------------")
print("Escriba una frase: ")
frase = input()
if not frase:
    print("No ha introducido ninguna frase")
    exit()
print("Escriba una vocal de la frase: ")
vocal = input()
vocal_con_tildes = {
    "a": "á",
    "e": "é",
    "i": "í",
    "o": "ó",
    "u": "ú"
}
frase_con_vocal_mayuscula = frase.replace(vocal, vocal.upper())
if vocal in vocal_con_tildes:
    frase_con_vocal_mayuscula = frase_con_vocal_mayuscula.replace(vocal_con_tildes[vocal], vocal_con_tildes[vocal].upper())
print("La frase con la vocal en mayúscula es: " + frase_con_vocal_mayuscula)