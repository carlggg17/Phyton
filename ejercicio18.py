# Ejercicio 18: Clasificador de letras en una palabra
palabra = input("Introduce una palabra: ")

vocales_referencia = "aeiouáéíóú"
vocales_encontradas = ""
consonantes_encontradas = ""

# Recorremos la palabra letra a letra
for letra in palabra:
    if letra.lower() in vocales_referencia:
        # Si la letra (en minúscula) está en nuestra lista de vocales
        vocales_encontradas += letra
    elif letra.isalpha():
        # Si es una letra pero no estaba en las vocales, es consonante
        consonantes_encontradas += letra

print(f"Las vocales de la palabra {palabra} son: {vocales_encontradas}")
print(f"Las consonantes de la palabra {palabra} son: {consonantes_encontradas}")