#Ejercicio13: Controlar la longitud de una frase
frase = input("Introduce una fraes: ")
#usamos len para calcular el numero de caracteres
longitud = len(frase)
print(f"La frase tiene {longitud} caracteres")
#Condicionales:
if longitud == 11:
    print("La frase tiene 11 caracteres")
elif longitud < 11:
    print("La frase tiene menos de 11 caracteres")
else:
    print("La frase tiene mas de 11 caracteres")