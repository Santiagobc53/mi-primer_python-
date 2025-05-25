# Programa para calcular el salario de un empleado con recargos según edad y horas trabajadas

codigo = input("Ingrese el código del empleado: ")
edad = int(input("Ingrese la edad del empleado: "))
horas_trabajadas = int(input("Ingrese las horas trabajadas: "))
valor_hora = float(input("Ingrese el valor por hora trabajada: "))
descuento = float(input("Ingrese el valor del descuento: "))

# Salario base
salario_base = horas_trabajadas * valor_hora
recargo = 0  # Inicialmente no hay recargo

# Condiciones de recargo
if edad > 60 and horas_trabajadas > 80:
    recargo = 1.20  # 120%
elif edad > 40 and horas_trabajadas > 160:
    recargo = 0.80  # 80%
elif edad > 20 and horas_trabajadas > 140:
    recargo = 0.60  # 60%
elif edad < 30 and horas_trabajadas > 120:
    recargo = 0.30  # 30%

# Cálculo del recargo y salario total
valor_recargo = salario_base * recargo
salario_total = salario_base + valor_recargo - descuento

# Mostrar resultados
print("\n--- Resultado ---")
print("Código del empleado:", codigo)
print("Salario base: $", round(salario_base, 2))
print("Recargo aplicado: $", round(valor_recargo, 2))
print("Descuento: $", round(descuento, 2))
print("Salario total a pagar: $", round(salario_total, 2))
