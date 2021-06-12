numeroMagico = 12345679 
numeroUsuario = int(input("ingrese numero entre 1 y 9"))
if(numeroUsuario<1 or numeroUsuario>9):
    print("debe ser un numero entre 1 y 9")
else:
    numeroMagico*=numeroUsuario*9
    print(numeroMagico)

