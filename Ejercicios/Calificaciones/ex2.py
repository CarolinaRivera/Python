
# 2. Calcular el área y perímetro de un círculo.

#print("Calcula el area de un circulo")

pi = 3.1416
print("Ingresa un valor para radio: ")
radius = int(input())


circulo_area = pow(radius, 2) * 3.1416
circulo_perimetro = (2* pi *radius)

print(f"el area de un circulo es {circulo_area}")
print(f"El perimetro de un circulo es {circulo_perimetro}")

