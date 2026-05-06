# Ejercicio 16: Deletrear una palabra con su índice numerico
palabra = input("Introduce una palabra: ")

# Usamos enumerate() nos da dos cosas: el índice (0, 1, 2...) y el valor (letra)
for posicion, letra in enumerate(palabra):
    print(f"En la posición {posicion} está la {letra}")