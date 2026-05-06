#Ejercicio14: BUCLES, un programa que cuente todos los numeros pares hasta el 50
pares = 0
impares = 0
for i in range(1, 51):
    if i % 2 == 0:

        pares = pares + 1
    else:
        impares = impares + 1
    
print(f"El total de numeros pares es de: {pares} ")
print(f"El total de numeros impares es de: {impares} ")