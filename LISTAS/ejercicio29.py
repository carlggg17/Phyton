# Ejercicio 29: Análisis de tipos de datos en una lista
lista1 = ['a', 'b', 'D', 'x', 'r', 'X', '3', 'h', 'w', '2', 'i']

# Inicializamos los contadores
cantidad_numeros = 0
cantidad_letras = 0
cantidad_mayusculas = 0
suma_numeros = 0

# Recorremos la lista elemento a elemento
for elemento in lista1:
    # Comprobamos si es un número (como string)
    if str(elemento).isnumeric():
        cantidad_numeros += 1
        suma_numeros += int(elemento) # Lo convertimos a entero para sumar
    
    #Comprobamos si es una letra
    elif str(elemento).isalpha():
        cantidad_letras += 1
        #  Comprobamos si esa letra es mayúscula
        if str(elemento).isupper():
            cantidad_mayusculas += 1

# Presentamos los resultados
print(f"Número de valores: {len(lista1)}")
print(f"Cantidad de números: {cantidad_numeros}")
print(f"Cantidad de letras: {cantidad_letras}")
print(f"Cantidad de mayúsculas: {cantidad_mayusculas}")
print(f"Suma total de números: {suma_numeros}")