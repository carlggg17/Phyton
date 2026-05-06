#Ejercicio20
pares = 0
impares = 0
positivos = 0
negativos = 0
ceros = 0
sumatotal = 0

numero = int(input("Introduce un numero: "))
#BUCLE se repite mientras no sea -99
while numero != -99:
    # f) Sumar el número al total
    sumatotal += numero

    # a) y b) Comprobar par o impar
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    # c), d) y e) Comprobar signo
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    else:
        ceros += 1

    # ¡IMPORTANTE! Volver a pedir el número al final del bucle
    # para que la condición del while se vuelva a evaluar
    numero = int(input("Introduce un número: "))

# Al salir del bucle (porque introdujo -99), mostramos las estadísticas
print("\nRESUMEN")
print(f"El número de pares es {pares}")
print(f"El número de impares es {impares}")
print(f"El número de positivos es {positivos}")
print(f"El número de negativos es {negativos}")
print(f"El número de ceros es {ceros}")
print(f"El total es {sumatotal}")