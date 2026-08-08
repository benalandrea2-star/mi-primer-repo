# ------------------------------------------------------------
# Programa: 3. Promedio de Notas
# Estudiante: Laura Andrea Benavides Alzate
# Asignatura: Fundamentos de Programación 1
# Fecha: 14/07/2026
# Descripción:
# Este programa solicita las tres notas de un estudiante
# y calcula el promedio final.
# ------------------------------------------------------------

# Programa para calcular el promedio de notas

print("Ingrese la primera nota:")
nota1 = float(input())

print("Ingrese la segunda nota:")
nota2 = float(input())

print("Ingrese la tercera nota:")
nota3 = float(input())

# Cálculo del promedio
promedio = (nota1 + nota2 + nota3) / 3

print("")

print(f"La primera nota es: {nota1}")
print(f"La segunda nota es: {nota2}")
print(f"La tercera nota es: {nota3}")

print("")

print(f"El promedio final del estudiante es: {promedio:.2f}")