salario, horasExtras, bonificacion = input().split()
salario = float(salario)
horasExtras = int(horasExtras)
bonificacion = int(bonificacion)

horaTrabajo = salario/186
valorExtra = horaTrabajo*0.35
porctBonificacion = salario*0.055*bonificacion
salarioTotal = salario+((valorExtra+horaTrabajo)*horasExtras)+porctBonificacion
descSalud = salarioTotal*0.045
descPension = salarioTotal*0.045
descCaja = salarioTotal*0.03
pagoSueldo = salarioTotal-descCaja-descPension-descSalud

print(round(salarioTotal,1),round(pagoSueldo,1))
