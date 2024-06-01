# A function is a block of which runs when it is called.
# You can data, known as parameters, into a function.
# Functions can return data as a result.
# In a function is defined the def keyword.


# lets define a function
def greet_user():
    print("Hello, User!")
greet_user()

def aoa():
    print("Asalam O Alaekum, All the way from London")
aoa()

def aoa(name):
    print(f"Asalam O Alaekum, {name}!, Kaifa Haluk?")
aoa("Osaid")

def aoa(name = "Meray Payaray Bhai"):
    print(f"Asalam O Alaekum, {name}!, Kaifa Haluk?")

aoa()

def aoa(name = "Meray Payaray Bhai"):
    print(f"Asalam O Alaekum, {name}!, Kaifa Haluk?")

aoa("Osaid")

# Return  values

def square(number=1):
    return number * number
result = (square(9))
print(result)

def square(number=1):
    return number * number
print(square(9))


# Recursion
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(2))


# lambda function

def x(a):
    return a/2
x = lambda a: a / 2
print(x(4))

def x(a, b):
    return a * b

x = lambda a, b: a * b
print(x(2, 8))

# define 10 functios with def and lambda

# Addition
def add_def(a, b):
    return a + b
add_lambda = lambda a, b: a + b

# Subtraction
def subtract_def(a, b):
    return a - b
subtract_lambda = lambda a, b: a - b

# Multiplication
def multiply_def(a, b):
    return a * b
multiply_lambda = lambda a, b: a * b

# Division
def divide_def(a, b):
    return a / b if b != 0 else "Cannot divide by zero!"
divide_lambda = lambda a, b: a / b if b != 0 else "Cannot divide by zero!"

# Square
def square_def(a):
    return a ** 2
square_lambda = lambda a: a ** 2

# Maximum
def max_def(a, b):
    return a if a > b else b
max_lambda = lambda a, b: a if a > b else b

# Length of string
def len_def(s):
    return len(s)
len_lambda = lambda s: len(s)

# Reverse string
def reverse_def(s):
    return s[::-1]
reverse_lambda = lambda s: s[::-1]

# Power
def power_def(a, b):
    return a ** b
power_lambda = lambda a, b: a ** b

# Check if even
def is_even_def(a):
    return a % 2 == 0
is_even_lambda = lambda a: a % 2 == 0
