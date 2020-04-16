# This program calculates basic math
# CTI-110
# P4HW2 - BasicMath
# Devorick Johnson
# 16 April 2020

# Define sum (adds two numbers)

def add(x, y):
        return x + y

# define function (subtracts two numbers)

def subtract (x, y):
        return x - y

# define function (multiplies two numbers)

def multiply (x, y):
        return x * y

# define function (divides two numbers)

def divide (x, y):
        return x / y

num1 = float(input('Enter First Number: '))
num2 = float(input('Enter Second Number: '))

print('----MENU----')
print('1.Add')
print('2.Multiply')
print('3.Subtract')
print('4.Exit')
print('------------')

# Take input from the user
choice = input('Enter choice(1/2/3/4): ')


if choice == '1':
    print(num1, '+', num2, '=', add(num1,num2))

if choice == '2':
    print(num1, '*', num2, '=', multiply(num1,num2))

if choice == '3':
    print(num1, '-', num2, '=', subtract(num1,num2))

elif choice == '4':
        print('Program Terminated')
else:
    print('select another MENU option')

print('----MENU----')
print('1.Add')
print('2.Multiply')
print('3.Subtract')
print('4.Exit')
print('------------')

# Take input from the user
choice = input('Enter choice(1/2/3/4): ')
if choice == '1':
    print(num1, '+', num2, '=', add(num1,num2))

if choice == '2':
    print(num1, '*', num2, '=', multiply(num1,num2))

if choice == '3':
    print(num1, '-', num2, '=', subtract(num1,num2))

elif choice == '4':
        print('Program Terminated')
else:
    print('select another MENU option')
        
