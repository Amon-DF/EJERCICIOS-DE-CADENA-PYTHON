print("Escribir un programa que pida al usuario que introduzca una frase y una vocal, y después muestre la misma frase, pero con la vocal introducida en mayúscula")
print ("----------------------------------------------------------------")
frase = input("Escriba una frase: ")
if not frase:
    print("No ha introducido ninguna frase")
    exit()
vocal = input("Escriba una vocal de la frase: ")
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