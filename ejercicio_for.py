#sacar el promedio
#no olvidar convertir a entero los datos que ingrese por teclado
#no olvidar convertir a string cuando vaya a imprimir por pantalla
usuario = int(input("Cuantos números desea ingresar: "))
suma=0
numero=0
for i in range(1,usuario+1):
    numero = int(input(f"ingrese el {i} numero: "))
    suma = numero + suma
promedio = suma/usuario 
print("el promedio es: " + str(promedio))
    
