x = 10

if x > 10:
    print("x es mayor que 10")
elif x == 10:
    print("x es igual a 10")
else:
    print("x es menor que 10")

y = 15
z = 20

# ------------------------------------------

if y > 10 and z > 25:
    print("y es mayor que 10 z 25")

if y > 10 or z > 25:
    print("y es mayor que 10 o z 25")

if not x > 10:
    print("x no es mayor que 10")

# ------------------------------------------

is_member = True
age = 15

if is_member:
    if age >= 15:
        print("Puedes entrar")
    else:
        print("No puedes entrar, eres un mocoso")
else:
    print("No puedes entrar, No eres member")