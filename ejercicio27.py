# Ejercicio 27: Introducir números en una lista y ordenados
cantidad = int(input("¿Cuántos números vas a introducir?: "))

# Creamos una lista vacía para almacenar los números
lista_numeros = []

# Usamos un bucle for para pedir la cantidad exacta de números
for i in range(cantidad):
    numero = int(input("Introduce un número: "))
    # .append() añade el número al final de la lista
    lista_numeros.append(numero)

# El método .sort() ordena la lista de menor a mayor automáticamente
lista_numeros.sort()

# Presentamos el resultado final
print(lista_numeros)