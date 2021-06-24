# funciones
# Se crean con la palabra reservada def

"""
funcion a, escribe los numero de 1 a n donde n es mayor que 0

"""

def numeros(n):
    num = 1
    print("Los numeros de 1 a ", n, "son: ")
    while num <=n:
        print(num)
        num +=1

def main():
   # n = int(input("digite hasta donde quiere imprimir: "))
    numeros(7)

main()
