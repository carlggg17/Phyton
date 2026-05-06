import random

# Definimos la lista y el programa elige una palabra al azar
palabras = ["casa", "gato", "barco", "perro", "madera", "agua", "puente", "pantalon"]
secreta = random.choice(palabras)

# Inicializamos la variable de respuesta del usuario
intento = ""

#  Bucle que se repite mientras el usuario no acierte
# Usamos .lower() para evitar errores si el usuario usa mayúsculas
while intento.lower() != secreta:
    intento = input("Introduce la palabra secreta: ")
    
    # Comprobamos si ha acertado para mostrar el mensaje correspondiente
    if intento.lower() != secreta:
        print("SIGUE JUGANDO")
    else:
        print("ACERTASTE")