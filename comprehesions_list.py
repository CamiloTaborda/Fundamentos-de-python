squares = [x**2 for x  in range(1,11)]
# print('Cuadrados', squares)

celsius = [0, 10, 20, 30, 40]
fahrenheit = [(tem * 9/5) * 32 for tem in celsius]
# print('Temperatura:', fahrenheit)

# Numeros pares
evens = [x for x in range(1,20) if x%2 == 0]
# print(evens)

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(matrix)
print(transposed)