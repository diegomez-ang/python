#clase sobre el ciclo for

#numero = int(input("ingrese un número"))

#for i in range(0,numero+1):
#    print(f"contador: {i}")

# print("fin del codigo")

# -------- Validar si es una vocal -----

#print("programa para encontrar una vocal")


# letras=""
# while(letras != 'a' and letras != 'e' and letras != 'i' and letras != 'o' and letras !='u'):
#   letras = input("ingrese una letra: ")
#print("imprimiste una vocal")

# ----------- valida si es un numero primo   ----------







# ------ numeros pares 

"""
for i in range(0,101):
    if(i%2 == 0):
        print(f"es un numero par {i}")
print("fin del programa")
"""

cantidad = int(input("ingrese la cantidad de personas"))
mayor_edad=0
menor_edad=0
for i in range(cantidad):
    edad=int(input(f"ingrese la edad numero: {i}"))
    if(edad>=18):
        mayor_edad = mayor_edad+1
    else:
        menor_edad = menor_edad+1
print(f"existen {mayor_edad} mayores de 18 años")
print(f"existen {menor_edad} menores de 18 años")

