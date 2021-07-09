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
    
