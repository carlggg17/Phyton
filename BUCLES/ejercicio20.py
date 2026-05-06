pares = 0
impares = 0
positivos = 0
negativos = 0
ceros = 0
suma_total = 0

while True:
    numero = int(input("Introduce un número: "))
    
    # 1. Comprobamos SIEMPRE primero si es el valor de parada
    if numero == -99:
        break  # Sale del bucle inmediatamente sin contar el -99
    
    # 2. Si no es -99, empezamos a contar
    suma_total += numero

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    else:
        ceros += 1

print("\nRESUMEN")
print(f"El número de pares es {pares}")
print(f"El número de impares es {impares}")
print(f"El número de positivos es {positivos}")
print(f"El número de negativos es {negativos}")
print(f"El total es {suma_total}")