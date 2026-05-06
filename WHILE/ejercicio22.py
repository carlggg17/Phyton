# Ejercicio 22: Bucle while con confirmación de usuario
continuar = "s"

while continuar.lower() == "s":
    # Pedimos los números
    n1 = int(input("Introduce el primer número: "))
    n2 = int(input("Introduce el segundo número: "))
    
    # Mostramos el resultado
    print(f"El resultado de la suma es: {n1 + n2}")
    
    # Preguntamos si quiere seguir
    # Usamos .lower() para que funcione tanto si pone 's' como 'S'
    continuar = input("Deseas repetir la operación s/n: ")

print("Programa finalizado")