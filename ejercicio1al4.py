#Ejercicio1: Programar que pida 2 numeros enteros y realiza la suma correspondiente:
#El resultado sea igual a 7
num1 = int(input("Introduce el valor del primer numero entero: "))
num2 = int(input("Introduce el segundo valor: "))
print(f"El resultado es: {num1 + num2}")


#Ejercicio2: Realizar la version con decimales
num3 = float(input("Introduce el numero decimal a sumar: "))
num4 = float(input("Introduce la suma del otro decimal: "))
print(f"El resultado de la suma decimal es de: {num3 + num4}")

#Ejercicio 3
#Programar que calcule dos operandos con los 7 operadores vistos en clase:  Con los numeros 2 y 3 como valores:
operador1 = 2
operador2 = 3
#SUMA
print(F"la suma de 2 + 3: {operador1 + operador2}")
#RESTA
print(f"la resta es: {operador1 - operador2}")
#MULTIPLICACION
print(f"La multiplicación es: {operador1 * operador2}")
#DIVISION
print(f"La division es de: {operador1 / operador2}")
#EXPONENTE
print(f"El exponente es: {operador1 ** operador2}")
#DIVISION ENTERA:
print(f"La division entera es: {operador1 // operador2}")

#Ejercicio 4
#PETICION DE HORAS Y QUE SE MUESTRE LAS HORAS Y SEGUNDOS.
hora = int(input("Introduce el numero de horas a calcular: "))
minutos = hora * 60
segundos = minutos * 60
print(f"El total de minutos es de: {hora * minutos}")
print(f"El total de segundos es de: {segundos}")


