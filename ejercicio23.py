# Variables: 
suma_acumulada = 0
repeticiones = 0
continuar = "s"

while continuar.lower() == "s":
    # Pedimos los números
    n1 = int(input("Introduce el primer número: "))
    n2 = int(input("Introduce el segundo número: "))
    
    # Calculamos la suma actual
    suma_actual = n1 + n2
    print(f"El resultado de la suma es: {suma_actual}")
    
    # Actualizamos las estadísticas
    suma_acumulada += suma_actual  # Sumamos el resultado al total general
    repeticiones += 1              # Sumamos una repetición
    
    # Preguntamos si quiere seguir
    continuar = input("Deseas repetir la operación s/n: ")

# Al salir del bucle, mostramos el resumen solicitado:
print(f"\nResumen: La suma total es de {suma_acumulada} y el número de repeticiones es de: {repeticiones}")