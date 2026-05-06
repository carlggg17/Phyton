import random

#  Definimos la lista de palabras
palabras = ["casa", "gato", "barco", "perro", "madera", "agua", "puente", "pantalon"]
secreta = random.choice(palabras)

# Desordenamos las letras de la palabra elegida
# random.sample toma las letras y las devuelve en una lista con orden aleatorio
letras_desordenadas = random.sample(secreta, len(secreta))
print(letras_desordenadas)

#  Lógica de los 3 intentos
intentos = 0
acertado = False

while intentos < 3 and not acertado:
    respuesta = input("Introduce palabra correcta: ").lower()
    
    if respuesta == secreta:
        print("Acertaste")
        acertado = True
    else:
        print("no has acertado")
        intentos += 1

# Mensaje final si agota los intentos
if not acertado:
    print("no has acertado ninguno de los intentos")