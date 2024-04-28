# Test the functions

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

def power(base, exponent):
    return base ** exponent

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def modulo(m, n):
    return m%n

result = add(5, 3)
print("5 + 3 =", result)

result = subtract(7, 2)
print("7 - 2 =", result)

result = multiply(4, 6)
print("4 * 6 =", result)

result = divide(8, 2)
print("8 / 2 =", result)

result = power(8, 2)
print("8 ^ 2 =", result)

result = factorial(5)
print("Factorial of 5 =", result)

result = modulo(15,5)
print("15%5 =", result)