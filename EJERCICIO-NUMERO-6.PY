print("Escribir un programa que pregunte el correo electrónico del usuario y muestre otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio *ceu.es*")
print ("----------------------------------------------------------------")
correo = input("Escriba su correo electrónico: ")
if not correo or "@" not in correo:
    print("El correo electrónico no es válido")
    exit()
nombre_usuario = correo.split("@") [0]
nuevo_correo = nombre_usuario + "@ceu.es"
print("Su nuevo correo electrónico es: " + nuevo_correo)