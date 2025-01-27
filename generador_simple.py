def my_generador():
    yield 1
    yield 2
    yield 3

for value in my_generador():
    print(value)

# Fibonacci

def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b
    
for num in fibonacci(10):
    print(num)