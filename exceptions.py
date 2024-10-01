try:
    divisor = int(input("Ingresa un numero divisor:"))
    result = 100/divisor
    print(result)
except ZeroDivisionError as e:
    print("Error: El divisor no puede ser cero")
except ValueError:
    print("Error: Debes introdicuir un numero valido")    
