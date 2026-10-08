#Variables
edad = int(input("Escribe tu edad: "))

#Opciones de acuerdo a la edad
if edad <= 12: print("$40 pesos el boleto")
elif edad >= 13 and edad <= 17:
    print("$60 pesos el boleto")
elif edad >= 18 and edad <= 59: 
    print("$80 pesos el boleto")
else: print("$50 pesos el boleto")