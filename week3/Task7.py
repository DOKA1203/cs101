def addition(a, b):
    return a + b
def subtraction(a, b):
    return a - b
def multiplication(a, b):
    return a * b
def division(a, b):
    if b == 0:
        return "Error"
    return a / b

a, b = 10, 5

print(addition(a, b))
print(subtraction(a, b))
print(multiplication(a, b))
print(division(a, b))
