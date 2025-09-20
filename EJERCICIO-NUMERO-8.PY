print("Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato *dd/mm/aaaa* y muestre por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter")
print ("--------------------------------------------------------------")
print("Escriba su fecha de nacimiento (dd/mm/aaaa): ")
fecha_nacimiento = input()
if not fecha_nacimiento or "/" not in fecha_nacimiento or fecha_nacimiento.count("/") != 2:
    print("La fecha de nacimiento no es válida")
    exit()
dia = fecha_nacimiento.split("/") [0]
mes = fecha_nacimiento.split("/") [1]
año = fecha_nacimiento.split("/") [2]
if len(dia) == 1:
    dia = "0" + dia
if len(mes) == 1:
    mes = "0" + mes
print("Usted nació el día " + dia + ", del mes " + mes + ", del año " + año)