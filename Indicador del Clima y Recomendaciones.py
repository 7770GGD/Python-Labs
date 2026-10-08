#Variables
lluvia = input("¿Está lloviendo? (si/no): ")
temperatura = int(input("¿Cuál es la temperatura?: "))
indice_calidad_aire = int(input("¿Cuál es el índice de calidad del aire? (0-500): "))

#LLuvia
if lluvia == "si":
    print("Lleva un paraguas.")
else:
    print("No necesitas un paraguas.")

#Temperatura
if temperatura >= 20 and temperatura <=25:
    print("La temperatura es agradable, diviértete.")
else:
    print("La temperatura no es agradable, cuidate.")

#Índice de calidad del aire
if indice_calidad_aire >= 0 and indice_calidad_aire <= 50 or indice_calidad_aire >= 51 and indice_calidad_aire <= 100:
    print("La calidad del aire es buena.")
elif indice_calidad_aire >= 101 and indice_calidad_aire <= 150:
    print("La calidad del aire es moderada.")
elif indice_calidad_aire >= 151 and indice_calidad_aire <= 200:
    print("La calidad del aire es mala.")
elif indice_calidad_aire >= 201 and indice_calidad_aire <= 300:
    print("La calidad del aire es muy mala.")
else:
    print("La calidad del aire es peligrosa You're cooked")