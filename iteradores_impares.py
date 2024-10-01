#  Crear un iterador para numeros impares 

# Limite
limit = 10

# Crear un iterador
odd_itter = iter(range(1, limit + 1, 2))

# Usar iterador
for num in odd_itter:
    print(num)  # Imprime los números impares del 1 al 9
