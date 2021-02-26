# 5. Pedir la cantidad de grados y convertirlos a °C, °F y K. census, fahrenheit kelvin

print("Ingresa un valor en grados Celsius para convertirlo a grados Fahrenheit y kepler")
grados_en_celsius = float(input())

fahrenheit = (grados_en_celsius * (9/5)) + 32
print(f"Los grados en Celsius {grados_en_celsius}, sera en grados fahrenheit {fahrenheit}")

kelvin = grados_en_celsius + 273.15
print(f"Los grados en Celsius {grados_en_celsius}, sera en grados Kelvin {kelvin}")


