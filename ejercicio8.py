#Programar que se introduzca 2 numeros y que devuelva cual es mayor, menor o iguales( SOLO NUEMOS DEL 0 AL 10)
num1 = int(input("Introduce un numero para comprobar si es mayor o menor: "))
num2 = int(input("Introduce otro numero: "))

#Comprobamos que esten dentro del rango indicado en el anunciado:
if num1 >= 0 and num1 <= 10 and num2 >= 0 and num2 <= 10:

    if num1 > num2:
        print(f"El numero {num1} es mayor que {num2}")

    elif num2 > num1:
        print(f"El numero {num2} es mayor que {num1}")

    else:
        print("Ambos numeros son iguales")

else:
    print("Alguno de los numeros no se indican en el enunciado")
