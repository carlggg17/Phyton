#Ejercicio10: Comprobar si la letras es MAYUSCULKA
letra = input("Introduce la letra: ")

#Introducimos el metodo   ISUPPER devuelve TRUE si la letra es mayuscula
if letra.isupper():
    print("La letra es mayuscula")
else:
    print("La letra es minuscula")


#Ejercicio11: Mejorar al poner un numero que salga una alerta
letra = input("Introduce la letra: ")

if letra.isnumeric():
    print("Has introducido un número, no una letra.")
elif letra.isalpha():
    
    if letra.islower():
        print("La letra introducida es una minúscula.")
    else:
        print("La letra introducida es una MAYÚSCULA.")

# Si no es número ni letra, es un símbolo
else:
    print("Has introducido un símbolo o carácter especial.")

