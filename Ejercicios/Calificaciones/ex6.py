
# 6. Obtener valores para: a, b y c. Calcular la fórmula general.

import math

print("ingresa los valores para la creacion de la formula general")

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

# pow(number1, 0.5)
x1 = (-b + pow(( b ** b )-(4 * a * c), 0.5))  / (2 * a)
x2 = (-b - pow(( b ** b )-(4 * a * c), 0.5))  / (2 * a)

x3 = (-b + math.sqrt(( b ** b )-(4 * a * c))) / (2 * a)
x4 = (-b - math.sqrt(( b ** b )-(4 * a * c))) / (2 * a)

#x2 = (b + (( b ** b )-(4 * a * c))) / 2 * a

print(f" X! = ", x1)
print(f" X1 = ", round(x1, 2))
print(f" X2 = ", round(x2, 2))
print(f" X3 = ", round(x3, 2))
print(f" X4 = ", round(x4, 2))








