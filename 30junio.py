"""
    escriba una programa en python que permita crear una lista de palabras, para ello el programa tiene que pedir un numero y luego soliciitar ese numero de palabras para crear la lista, por ultimo el programa tiene que escribir la lista.
"""
def crear_lista():
    cont = 0
    lista_nombres = []
    salir = False
    while not salir:
        lista_nombres.append(input(f"Digite el nombre {cont+1}: "))
        cont +=1
        respuesta = input("desea ingresar otro nombre? (S/N)")
        if respuesta.upper() == "N":
            salir = True

    print(lista_nombres)


def main():
    print("MAjenar listas")
    crear_lista()

main()
