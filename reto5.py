# analizar el enunciado.
#kerwin carlos torres castillo
#crear base de datos simulada con un diccionario, con lista incluida

#2. construr 3 funciones agragar actualizar y borrar, como funciones independientes
# split convierte una string y lo convierte una lista

def agregar():
    if items[0] in productos:
        print('error')
    else :
        key = items[0]
        items.pop(0)
        productos[key] = items

def actualizar():
    if items[0] not in productos:
        print('error')
    else:
        key = items[0]
        items.pop(0)
        productos[key] = items

def eliminar():
    if items[0] not in productos:
        print('error')
    else:
        key=items[0]
        productos.pop(key)
def promedio():
    suma=0
    for i in productos.values():
        suma+=i[1]
    prom= round(suma/len(productos),1)
    return prom
def inventario():
    for i in productos.values():
        total=i[1]*i[2]
    
    return total
def mayor():
    mayor=0
    for i in productos.values():
        if i[1]>mayor:
            mayor=i[1]
            nombreMayor = i[0]
    return nombreMayor
def menor():
    menor=200000
    for i in productos.values():
        if i[1]<menor:
            menor=i[1]
            nombreMenor = i[0]
    return nombreMenor




productos = {
    1:['Tangelos', 9000.0, 67],
    2:['Limones', 2500.0, 35],
    3:['Peras', 2700.0, 65],
    4:['Arandanos', 9300.0, 34],
    5:['Tomates', 8100.0, 42],
    6:['Fresas', 9100.0, 90],
    7:['Helado', 4500.0, 41],
    8:['Galletas', 700.0, 18],
    9:['Chocolates', 4500.0, 80],
    10:['Jamon', 11000.0, 55]
}

operacion = input('que operacion va a realizar: ').upper()
items = input().split()
items[0] = int(items[0])
items[2] = float(items[2])
items[3] = int (items[3])

#definir funciones

if operacion == 'AGREGAR':
   con = agregar()
elif operacion == 'ACTUALIZAR':
    con = actualizar()
elif operacion == 'ELIMINAR':
    con = eliminar()


print(mayor(), menor(), promedio(), inventario())

