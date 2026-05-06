# Ejercicio 21: Bucle while controlado por el contador
veces = int(input("¿Cuántas veces quieres que repita la frase?: "))

# Inicializamos el contador en 0
contador = 0

# El bucle se ejecutará mientras el contador sea menor que el número pedido
while contador < veces:
    print("buenos días")
    
    # IMPORTANTE: Incrementamos el contador en 1 en cada vuelta par que el bucle no sea infinito
    contador += 1