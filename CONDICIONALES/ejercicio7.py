#Programar que se introduzca 2 numeros y que devuelva cual es mayor, menor o iguales
num1 = int(input("Introduce un numero para comprobar si es mayor o menor: "))
num2 = int(input("Introduce otro numero: "))

if num1 > num2:
    print(f"El numero {num1} es mayor que {num2}")

elif num2 > num1:
    print(f"El numero {num2} es mayor que {num1}")

else:
    print("Ambos numeros son iguales")

