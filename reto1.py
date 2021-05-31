print("Calculo de parafiscales")
#valor hora laboral se obtiene dividiendo el salario sobre 186
salario_base = float(input("ingrese su salario base: "))
horas_extra = float(input("ingrese sus horas extras: "))
bonificaciones = float(input("ingrese bonificaciones: "))

# valor hora de trabajo normal
hora_trabajo = salario_base/186
#hora extra
horas_extra = hora_trabajo + (hora_trabajo*0.35)
#beneficio
beneficio = salario_base * 0.055
#descuento salud
descuento_salud = salario_base * 0.045
#descuento pension
descuento_pension = salario_base * 0.045
#descuento caja
descuento_caja = salario_base *0.03




print("salario basico: " + str(salario_base))
print("horas extra: " + str(horas_extra))
print("bonificaciones: " + str(bonificaciones))