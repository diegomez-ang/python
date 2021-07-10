import os
os.system("cls")
alfabeto = ["a", "z", "c", "g", "l", "p", "d"]
alfabeto_ordenado = sorted(alfabeto, reverse=True)
#El sorted lo que hace es crear una nueva lista sin afectar la original
print(alfabeto)
print(alfabeto_ordenado)

print("-----------------------------------------")

lista = ["o", "a", "l", "r", "g"]
print("Lista original", lista)
for i in range(0, len(lista)):
    if lista[i] == "o":
        lista[i] = 40
print("lista remplazo", lista)
print("-----------------------------------------")
mi_lista = ["cadena de caracteres", 0, 2, "otro", "aceptar"]

indice = mi_lista[0].find("t")
print (indice)

indice = mi_lista[3].find("r")
print(indice)
print("-----------------------------------------")

#El .pop si no le pongo parametro me borra el último, el remove me borra el primero
#El .pop me borra el indice que le voy a indicar
#El .clear me borra todos los datos

seguir = True
while seguir:
    os.system("cls")
    listado = []
    palabras = int(input("Digite el numero de palabras: "))
    for i in range(palabras):
        listado.append(input(f"Digite el {i}° nombre: "))
    print("Los nombres que ingresaste fueron")
    for i in range(palabras):
        print(listado[i])
    print("-----------------------------------------")
    
    repetidos = 0
    buscar = input("Digite el nombre que desea encontrar: ")
    for i in range(palabras):
        if listado[i] == buscar:
            repetidos += 1
    print(f"Las veces que se repite el nombre {buscar} son: {repetidos}")
    print("-----------------------------------------")

    """reemplazar = input("Digite el nombre que desea usar para reemplazar: ")
    reemplazado = input("Digite el nombre a reemplazar")
    for i in range(palabras):
        if listado[i] == reemplazado:
            listado[i] = reemplazar
    print(f"La lista actual es {listado}")
    print("-----------------------------------------")"""

    eliminar = input("Digite el nombre a eliminar: ")
    borrado = ""
    for i in range(palabras):
        if listado[i] == eliminar:
            listado[i] = borrado
    print(f"La lista actual es: {listado}")
    respuesta = input("Desea repetir la sección e intentar nuevamente? S/N: ")
    if respuesta == "N":
        seguir = False
