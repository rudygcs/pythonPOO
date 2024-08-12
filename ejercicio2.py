# Solicitar el sueldo base y el valor de ventas realizadas al usuario
sueldo_base = float(input("Ingrese el sueldo base: "))
ventas_realizadas = float(input("Ingrese el valor de ventas realizadas: "))

# Calcular la comisión por ventas (10% del total vendido)
comision_ventas = 0.10 * ventas_realizadas

# Calcular el IGSS (4.83% del sueldo base)
igss = 0.0483 * sueldo_base

# Calcular el ahorro (7% del total ganado)
ahorro = 0.07 * (sueldo_base + comision_ventas)

# Calcular el total ganado (sueldo base + comisión por ventas + bonificación)
total_ganado = sueldo_base + comision_ventas + ahorro

# Calcular el total de descuentos (ahorro + IGSS)
total_descuentos = ahorro + igss

# Calcular el sueldo líquido (Total ganado - total descuentos)
sueldo_liquido = total_ganado - total_descuentos

# Mostrar los resultados
print(f"Comisión por ventas: {comision_ventas}")
print(f"IGSS: {igss}")
print(f"Ahorro: {ahorro}")
print(f"Total ganado: {total_ganado}")
print(f"Total descuentos: {total_descuentos}")
print(f"Sueldo líquido: {sueldo_liquido}")