print("¿Qué operación quieres realizar?")
print("1. Suma")
print("2. Resta")
print("3. División (No se puede dividir entre cero)")
print("4. Multiplicación")
print("5. Exponente")

operación = int(input("Ingrese el número de la operación que desea realizar: "))

if operación == 1:
    suma = float(input("Ingrese el primer número para la suma: ")) + float(input("Ingrese el segundo número para la suma: "))
    print("El resultado de la suma es: ", suma)

elif operación == 2:
    resta = float(input("Ingrese el primer número para la resta: ")) - float(input("Ingrese el segundo número para la resta: "))
    print("El resultado de la resta es: ", resta)

elif operación == 3:
    numerador = float(input("Ingrese el primer número para la división: "))
    divisor = float(input("Ingrese el segundo número para la división: "))
    if divisor != 0:
        división = numerador / divisor
        print("El resultado de la división es: ", división)
    else:
        print("Error: No se puede dividir entre cero.")

elif operación == 4:
    multiplicación = float(input("Ingrese el primer número para la multiplicación: ")) * float(input("Ingrese el segundo número para la multiplicación: "))
    print("El resultado de la multiplicación es: ", multiplicación)

elif operación == 5:
    exponente = float(input("Ingrese el primer número para el exponente: ")) ** float(input("Ingrese el segundo número para el exponente: "))
    print("El resultado del exponente es: ", exponente)

else:
    print("Operación no válida. Ingrese un número del 1 al 5.")