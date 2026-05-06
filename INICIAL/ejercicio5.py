#Al ser una operacion matematica empezamos con un modulo import math:
import math
numero = float(input("Introduce un numero para calcular su raiz cuadrada: "))
#aqui calculamos la raiz cuadrada del numero
raiz = math.sqrt(numero)
#Mostramos la division entera con //
rfinal = raiz // 2
print(f"La raiz cuadrada de {numero} es : {raiz}")
print(f"Su division entera es: {rfinal}")
