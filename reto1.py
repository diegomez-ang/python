print("Calculo de parafiscales")
#valor hora laboral se obtiene dividiendo el salario sobre 186
salario_base = float(input("ingrese su salario base: "))
h_extraRealizadas = float(input("ingrese sus horas extras: "))
bonificaciones = float(input("ingrese bonificaciones: "))

# valor hora de trabajo normal
hora_trabajo = salario_base/186
#hora extra
horas_extra = hora_trabajo + (hora_trabajo*0.35)
#beneficio
beneficio = salario_base * 0.055
#salario total
salario_total = salario_base + (horas_extra*h_extraRealizadas) + beneficio
#descuento salud
descuento_salud = salario_total * 0.045
#descuento pension
descuento_pension = salario_total * 0.045
#descuento caja
descuento_caja = salario_total *0.03
# sueldo pagado
salario_pagado = salario_total - descuento_caja - descuento_pension - descuento_salud

print("salario bruto: " + str(salario_total))
print("salario pagado: " + str(salario_pagado))
