
# 6. Obtener valores para: a, b y c. Calcular la fórmula general.

import math

print("ingresa los valores para la creacion de la formula general")

a = float(input())
b = float(input())
c = float(input())

# pow(number1, 0.5)
x1 = (-b + pow(( b ** b )-(4 * a * c), 0.5))  / (2 * a)
x2 = (-b + math.sqrt(( b ** b )-(4 * a * c))) / (2 * a)
x3 = (-b - math.sqrt(( b ** b )-(4 * a * c))) / (2 * a)

#x2 = (b + (( b ** b )-(4 * a * c))) / 2 * a

print(x1)
print(x2)
print(x3)






