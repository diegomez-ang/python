import os
os.system("cls")

meses = ("Enero","Febrero", "Marzo", "Abril", "Mayo", "Junio","Julio", "agosto","Septiempre","Octubre", "Noviembre", "Diciembre")

print(len(meses))

salir = False
while not salir:
    numero = int(input("Digite el numero del mes = "))
    if (numero>=1 and numero<=12):
        print(meses[numero-1])
    else:
        print("ingrese un numero entre 1 y 1i2")
        salir = input("desea continuar S/N: ")
        if salir.upper() == "N":
            salir = True
        else: 
            salir = False

    meses = list(meses)
    print("tipo de datos = ", type(meses))
    print()
