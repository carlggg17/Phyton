#Calcular el indice de MASA CORPORAL 
#Pediremos el peso en kg y la estatura en metros
#IMC = peso / estatura al cuadrado
#Si el IMC es igual y mayor de 25 debe indicar que hay sobrepeso
peso = float(input("Introduce el peso en kg: "))
altura = float(input("Indica la altura en metros: "))

altura = altura / 100

imc = peso / (altura ** 2)

#Resultado:
print(f"Si pesas {peso} kilos y mides {altura} metros, tu ICM es: {round(imc, 2)} ")

#Condicion con el IF
if imc >= 25:
    print("Hay sobrepeso, debes bajarlo")
