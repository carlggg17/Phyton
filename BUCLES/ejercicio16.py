#Ejercicio17: Patron numericoi
for i in range(5, 0, -1):
    # En cada fila, imprimimos desde el valor de 'i' hasta el 1
    for j in range(i, 0, -1):
        print(j, end="") # end="" evita que salte de línea después de cada número
    #Para realizarsalto de linea para cada fila usamos print
    print()
    