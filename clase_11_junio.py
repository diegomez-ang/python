#suma dos numeros enteros positivos

#a = int(input("ingrese el primer numero: "))
#b = int (input("ingrese el segundo numero: "))
#c = a+b
#print("el resultado de la suma es" + c)

#if(a>0 and b>0):
 #   c = a+b
  #  print(f"el resultado de la suma es: {c}") #poner el  f para poder usar los {}
#else:
#    print("Numeros errados menso")
#print("eso es todo amigos :)")

# programa de cedula
from datetime import date
from datetime import datetime

#añoNacimiento = int(input("ingrese su año de nacimiento: "))
#mesNacimiento = int(input("ingrese su mes de nacimiento: "))
#diaNacimiento = int(input("ingrese su dia de nacimiento: "))

añoNacimiento, mesNacimiento, diaNacimiento = input("ingrese su fecha de nacimiento (YYYY/MM/DD): ").split("/")
añoNacimiento = int(añoNacimiento)
mesNacimiento = int(mesNacimiento)
diaNacimiento = int(diaNacimiento)

fecha = datetime.now()
day = int(fecha.day)
month = int(fecha.month)
year = int(fecha.year)

print(fecha)

if (mesNacimiento >0 and mesNacimiento<13):
    yearsOld = year - añoNacimiento
    print(f"años cumplidos: {yearsOld} ")
    if(yearsOld>=18):
        print("saca la cedula ya no eres un mocoso")
    else:
        print("aun eres un mocoso")
else:
    print("menso son solo 12 meses")