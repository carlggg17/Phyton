import random

# Definimos la lista con los valores del enunciado
objetos = ["casa", "gato", "barco", "perro", "madera", "agua", "puente", "pantalon"]

# Usamos el método choice para elegir uno al azar
seleccion = random.choice(objetos)

# Mostramos el resultado
print(f"El objeto seleccionado al azar es: {seleccion}")