def show_menu():
    print("1. Add Numbers")
    print("2. Greet User")
    print("3. Check Number Type")

def add_numbers(a, b):
    sum = a + b
    return sum

def greet_user(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

def check_number(num):
    if num > 0:
        return print("Positive")
    elif num < 0:
        return print("Negative")
    else:
        return print("Zero")

def square_number(c):
    return c ** 2
    
show_menu()
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = add_numbers(x, y)
print(f"Sum: {z}")
user_name = input("Enter your name: ")
greet_user(user_name)
number = int(input("Enter any number: "))
check_number(number)
num1 = int(input("Enter a number for square: "))
print(f"The square is: {square_number(num1)}")