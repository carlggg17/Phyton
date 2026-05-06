# Ejercicio 17: Patrón de asteriscos creciente y decreciente

# 1 Triángulo creciente (de 1 a 5 asteriscos)
for i in range(1, 6):
    print("*" * i)

# 2 Triángulo decreciente (de 4 a 1 asteriscos)
# Empezamos en 4, llegamos hasta 0 (no incluido) y bajamos de 1 en 1
for i in range(4, 0, -1):
    print("*" * i)