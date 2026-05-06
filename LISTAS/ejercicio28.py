# Ejercicio 28: Lista de caracteres sin duplicados y con confirmación s/n
lista_letras = []
continuar = "s"

while continuar.lower() == "s":
    letra = input("Introduce una letra: ")
    
    # Comprobamos si la letra NO está ya en la lista
    if letra not in lista_letras:
        lista_letras.append(letra)
    else:
        print(f"La letra '{letra}' ya ha sido introducida anteriormente.")
    
    # Preguntamos si el usuario quiere seguir añadiendo
    continuar = input("¿Deseas repetir s/n: ")

# Al finalizar el bucle, imprimimos la lista resultante
print(lista_letras)