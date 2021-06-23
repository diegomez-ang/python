#s = "hola pecuecas"
# print(s.count('e')) busca cuantas veces se repite algo 

#print(s.find('e'))
#print(s.index('a')) indica la posicion en la que esta la busqueda 
#print(s.find('W')) si no existe entrga -1


numero = int(input("ingrese un numero: "))
"""
#triangulo rectangulo
for i in range(numero):
    print('*' * i)
print("fin del programa")

"""

#flecha 
if(numero >0 and numero < 6):

    for i in range(numero):
        print("    *    ")
        print("   * *   ")
        print("  *   *  ")
        print(" *     * ")
        print("***   ***")
        print("  *   *  ")
        print("  *   *  ",end=" ")
        print("  *****  ",end=" ")
    
      #  print("    *     \n   * *    \n  *   *  \n *     * \n***   *** \n  *   *  \n  *   *  \n  *****  \n",end="    ")
else:
    print("fin del programa")
