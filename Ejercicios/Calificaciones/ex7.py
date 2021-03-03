
# 7. Pedir el nivel del agua en metros de una cisterna

print(" Cual es el nivel de agua en la cisterna")

water_level = float(input()) 

if (water_level >= 6):
    print("Desbordamiento de agua")
elif (water_level > 4 and water_level < 6):
#elif (4<+ water_level >= 6): 

    print("desacelerar bomba")
elif (water_level > 2 and water_level < 4):
#elif (2<= water_level >=4)

    print("Bomba trabajando")
elif (water_level >= 0 and water_level < 2):
#elif (0<= water_level >=2)

    print("Acelerar Bomba de Agua")
elif (water_level == 0):
    print("Encender Bomba de agua")
else:
    print("FUGA EN CISTERNA!")




# # Condicionales Mayoría de edad
# edad = 18

# if (edad >= 18):
#     print("Mayor de edad")
# elif (edad > 0 and edad < 18): # Operador lógico and, or, not
#     print("Menor de edad")
# else:
#     print("No válido")
