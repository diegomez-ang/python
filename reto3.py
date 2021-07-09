cantidad = int(input())

for i in range (0,cantidad):
    ancho, alto, peso, cilindraje, costo = input().split(" ")
    ancho = int(ancho)
    alto = int(alto)
    peso = int(peso)
    cilindraje = int(cilindraje)
    costo = int(costo)

if ancho < 2005 and alto < 950 and peso > 702 and cilindraje < 1600:
    print(costo)
else:
    print("NO DISPONIBLE")
