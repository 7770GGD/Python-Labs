num_1 = int(input("Introduce un número: "))

if num_1 % 2 == 0:
    print("La suma gaussiana es:", num_1 * (num_1 + 1) // 2)
else:
    print("El volumen de un dodecaedro es:", (15 + 7 * 5**0.5) / 4 * num_1**3)
