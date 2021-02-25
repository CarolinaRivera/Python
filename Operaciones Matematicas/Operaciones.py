
print("Escribe el numero1: ")
number1 = int(input())

print("Escribe numero2: ")
number2 = int(input())


suma = number1 + number2
resta = number1 - number2

potencia1 = pow(number1, number2)
potencia2 = pow(number1, number2)
raiz_cuadrada = pow(number1, 0.5)
raiz_cubica = pow(number1, 1/3)
modulo = number1 % number2

#suma
print("la suma es igual a " + str(suma))
print(f"la suma = {suma}")

#resta
print("la resta es igual a " + str(resta))
print(f"La resta = {resta}")

#multiplicacion
print(f"la multiplicaion de " + str(number1 * number2))

#division
print(f"la division de " + str(number1 / number2))

#potencias
print(f"La potencia de " + str(number1))
print(f"La potencia de " + str(number2))

#raices
print(f"La raiz cuadrada de " + str(raiz_cuadrada))
print(f"La raiz cubica de " + str(raiz_cubica))
print(f"La raiz cubica de ",  str(raiz_cubica))

#modulo
print(f"El modulo o residuo es " + str(modulo))
print(f"El modulo o residuo  = {modulo}")

