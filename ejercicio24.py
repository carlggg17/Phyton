# Ejercicio 24:
suma_acumulada = 0
repeticiones = 0

# El bucle se repite MIENTRAS el total sea menor o igual a 50
while suma_acumulada <= 50:
    # Pedimos los números
    n1 = int(input("Introduce el primer número: "))
    n2 = int(input("Introduce el segundo número: "))
    
    # Calculamos la suma de la operación
    suma_actual = n1 + n2
    suma_acumulada += suma_actual
    repeticiones += 1
    
    # Control del mensaje singular/plural para las operaciones
    palabra_operacion = "operación realizada" if repeticiones == 1 else "operaciones realizadas"
    
    # Mostramos los resultados por pantalla
    print(f"El resultado de la suma es: {suma_actual}")
    print(f"El total acumulado es: {suma_acumulada} y llevas {repeticiones} {palabra_operacion}")
    print("-" * 40) #separador lineas

print("Fin del programa")