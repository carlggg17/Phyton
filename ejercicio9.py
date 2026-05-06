import math

print("--- Resolución de Ecuación de Segundo Grado ---")
a = float(input("Introduce el coeficiente a: "))
b = float(input("Introduce el coeficiente b: "))
c = float(input("Introduce el coeficiente c: "))

# 1. Calculamos el discriminante

discriminante = b**2 - 4*a*c

# 2. Comprobamos si el discriminante es negativo
if discriminante < 0:
    print("La raíz no puede ser un valor negativo, no hay solución real.")
else:
    # 3. Calculamos las dos soluciones
    # math.sqrt() calcula la raíz cuadrada
    x1 = (-b + math.sqrt(discriminante)) / (2 * a)
    x2 = (-b - math.sqrt(discriminante)) / (2 * a)
    
    print(f"El valor de x1 es: {x1}")
    print(f"El valor de x2 es: {x2}")