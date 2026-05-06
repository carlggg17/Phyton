import random

#Empezamos los contadores para cada cara del dado
uno = 0
dos = 0
tres = 0
cuatro = 0
cinco = 0
seis = 0

# Realizamos el bucle de 100 tiradas
for i in range(100):
    resultado = random.randint(1, 6)
    
    #  Clasificamos el resultado
    if resultado == 1:
        uno += 1
    elif resultado == 2:
        dos += 1
    elif resultado == 3:
        tres += 1
    elif resultado == 4:
        cuatro += 1
    elif resultado == 5:
        cinco += 1
    elif resultado == 6:
        seis += 1

#  Presentamos los resultados por pantalla
print(f"Uno: {uno}")
print(f"Dos: {dos}")
print(f"Tres: {tres}")
print(f"Cuatro: {cuatro}")
print(f"Cinco: {cinco}")
print(f"Seis: {seis}")