#Ejercicio19

n1 = int(input("Introduce el primer intervalo: "))
n2 = int(input("Introduce el segundo intervalo: "))

resultados = []

# Caso A: El primer número es menor o igual al segundo (Ascendente)
if n1 <= n2:
    for i in range(n1, n2 + 1):
        resultados.append(str(i))

# Caso B: El primer número es mayor (Descendente)
else:
    # range(inicio, fin, paso) -> usamos -1 para bajar
    for i in range(n1, n2 - 1, -1):
        resultados.append(str(i))

# Unimos todos los números de la lista con un guion "-"
print("-".join(resultados))