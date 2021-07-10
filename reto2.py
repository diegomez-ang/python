
distanciaMetros, velocidadMaxima, tiempo = input().split(' ') 
distanciaMetros = float(distanciaMetros)
velocidadMaxima = float(velocidadMaxima)
tiempo = float(tiempo)

if distanciaMetros>=0 and velocidadMaxima>=0 and tiempo>0:
    velocidadMedia = distanciaMetros/tiempo
    velMaxSegundos = velocidadMaxima*1000/3600
    record=velMaxSegundos+(velMaxSegundos*0.25)
    if velocidadMedia<=velMaxSegundos:
        print('VELOCIDAD NORMAL')
    elif velocidadMedia<record:
        print('NUEVO RECORD')
    else:
        print('ENTREVISTA')
else:
    print('VALORES NEGATIVOS')
#programa velocidad
distSeparacion, recordActual, tiempo = input().split()

distSeparacion = float(distSeparacion)
recordActual = float(recordActual)
tiempo = float(tiempo)

velocidad = distSeparacion/tiempo



if(velocidad < recordActual):
    print("VELOCIDAD NORMAL")
elif(velocidad > recordActual):
    print("NUEVO RECORD")
elif(velocidad > recordActual + (recordActual*0.25)):
    print("ENTREVISTA")
    
