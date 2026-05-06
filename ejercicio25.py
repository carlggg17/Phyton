#Ejercicio25
import random

# El programa genera el número secreto
secreto = random.randint(1, 1000)
# Inicializamos el intento con un valor que no pueda ser el secreto
intento = 0
contador = 0

print("Juego: Adivina el número (1 al 1000)")

# El bucle se repite mientras el intento sea diferente al secreto
while intento != secreto:
    intento = int(input("Introduce un valor comprendido entre 1 y 1000: "))
    contador += 1
    
    if intento < secreto:
        print("El número que has introducido es menor")
    elif intento > secreto:
        print("El número que has introducido es mayor")

# Al salir del bucle, mostramos el éxito
print(f"Acertaste, has realizado {contador} intentos")