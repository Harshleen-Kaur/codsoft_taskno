def calculator(operator):
    if operator == '+':
        return add(number1,number2)
    elif operator == '-':
        return subtract(number1,number2)
    elif operator == '*':
        return multiply(number1,number2)
    elif operator == '/':
        return divide(number1,number2)
    elif operator == '%':
        return modulo(number1,number2)
    elif operator == '**':
        return exponent(number1,number2)
    else:
        print('Invalid operation')

def add(number1,number2):
    print(number1 + number2)

def subtract(number1,number2):
    print(number1  - number2)

def multiply(number1,number2):
    print(number1 * number2)

def divide(number1,number2):
    try:
        print(number1 / number2)
    except Exception as e:
        print(e)

def modulo(number1,number2):
    try:
        print(number1 % number2)
    except Exception as e:
        print(e)

def exponent(number1,number2):
    print(number1 ** number2)

chance = True   
while(chance == True):
    number1 = int(input('Enter the first number: '))
    number2 = int(input('Enter the second number: '))
    operator = input('Enter the arithmetic operator: ')
    calculator(operator)
    press = input('Do You Wish to Continue:y/n ')
    if press == 'n':
        chance = False
    
