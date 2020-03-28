import math
from random import randint

class Calculator:
    def __init__(self):
        pass

    #### Large Loop Functions
    # Addition

    def add(self,a,b):
        #print(a + b)
        return a+b

    # Subtraction

    def subtract(self, minuend,subtrahend):
        #print(minuend-subtrahend)
        return minuend-subtrahend

    # Multiplication

    def multiply(self, a,b):
        #print(a*b)
        return a*b

    # Division

    def divide(self, dividend,divisor):
        #print(dividend/divisor)
        return dividend/divisor

    # Square

    def square(self, base):
        #print(base ** 2)
        return base ** 2

    # Exponent

    def exp(self, base, exponent):
        #print(base**exponent)
        return base**exponent

    # Square Root

    def square_root(self, n):
        #print(n ** (1 / 2))
        return n ** (1 / 2)

    # Inverse / Reciprocal

    def inv(self, n):
        #print(1/n)
        return 1/n

    #### Trig

    def sine(self, x):
        #print(math.sin(x))
        return math.sin(x)

    def cosine(self, x):
        #print(math.cos(x))
        return math.cos(x)

    def tangent(self, x):
        #print(math.tan(x))
        return math.tan(x)

    def invSin(self, x):
        print(math.asin(x))
        return math.asin(x)

    def invCos(self, x):
        #print(math.acos(x))
        return math.acos(x)

    def invTan(self, x):
        #print(math.atan(x))
        return math.atan(x)

    # Switch Sign

    def switch_sign(self, n):
        #print(-1*n)
        return -1 * n

    # Factorial

    def factorial(self, n):
        #print(math.factorial(n))
        return math.factorial(n)

    # Log Base 10

    def log_base_10(self, n):
        #print(math.log10(n))
        return math.log10(n)

    # Inverse log 10^x

    def inv_log_10(self, n):
        #print(10**n)
        return 10**n

    # Log Base e

    def log_base_e(self, n):
        #print(math.log(n))
        return math.log(n)

    # Inverse ln

    def inv_log_e(self, n):
        #print(math.exp(n))
        return math.exp(n)

    # Log Base Custom

    def log_base_y(self, n, base):
        #print(math.log(n, base))
        return math.log(n, base)


    #### Small Loop Functions
    # Addition

    def add2(self, b):
        #print(main_result+b)
        return main_result+b

    # Subtraction

    def subtract2(self, subtrahend):
        #print(main_result-subtrahend)
        return main_result-subtrahend

    # Multiplication

    def multiply2(self, b):
        #print(main_result*b)
        return main_result*b

    # Division

    def divide2(self, divisor):
        #print(main_result/divisor)
        return main_result/divisor

    # Square

    def square2(self, base):
        #print(main_result ** 2)
        return main_result ** 2

    # Exponent

    def exp2(self, exponent):
        #print(main_result**exponent)
        return main_result**exponent

    # Square Root

    def square_root2(self, main_result):
        #print(main_result ** (1 / 2))
        return main_result ** (1 / 2)

    # Inverse / Reciprocal

    def inv2(self, main_result):
        #print(1/main_result)
        return 1/main_result

    #### Both Loop Functions

    # Enter num prompt

    def enter_num(self):
        num1 = float(input())
        return num1

    def choose_data_type(self):
        data_choice = int(input('Enter data type: 1. Decimal 2. Hexadecimal 3. Binary 4. Octal '))
        if data_choice == 1:
            print(main_result)
            return main_result
        elif data_choice == 2:
            print(hex(int(main_result)))
            return hex(int(main_result))
        elif data_choice == 3:
            print(bin(int(main_result)).replace("0b", ""))
            return bin(int(main_result)).replace("0b", "")
        elif data_choice == 4:
            print(oct(int(main_result)))
            return oct(int(main_result))

#### Large Loop ####

def choose_op():
    print('1 Addition           2 Subtraction       3 Multiplication        4 Division')
    print('5 Square             6 Power             7 Square Root           8 Inverse')
    print('9 Sin                10 Cos              11 Tan                  12 Switch Sign')
    print('13 invSin            14 invCos           15 invTan               16 Factorial')
    print('17 Log 10            18 10^x             19 Ln                   20 e^x')
    print('21 Log base          22 pi               23 Mole                 24 Random Number')
    print('25 M+                26 MRC              27 MC                   28 Exit')
    print(' ')
    op = int(input('Choose an operation: '))

    if op == 1:
        print('Addition')
        print('Enter the first addend: ')
        addend1 = calc.enter_num()
        print('Enter the second addend: ')
        addend2 = calc.enter_num()
        result = calc.add(addend1,addend2)
        return result

    elif op == 2:
        print('Subtraction')
        print('Enter the minuend: ')
        minuend = calc.enter_num()
        print('Enter the subtrahend: ')
        subtrahend = calc.enter_num()
        result = calc.subtract(minuend, subtrahend)
        return result

    elif op == 3:
        print('Multiplication')
        print('Enter the first factor: ')
        a = calc.enter_num()
        print('Enter the second factor: ')
        b = calc.enter_num()
        result = calc.multiply(a,b)
        return result

    elif op == 4:
        print('Division')
        print('Enter the dividend: ')
        dividend = calc.enter_num()
        print('Enter the divisor: ')
        divisor = calc.enter_num()
        if divisor == 0:
            print('ERROR')
            return None
        else:
            result = calc.divide(dividend,divisor)
            return result

    elif op == 5:
        print('Square')
        print('Enter a number to square: ')
        base = calc.enter_num()
        result = calc.square(base)
        return result

    elif op == 6:
        print('Power')
        print('Enter the base')
        base = calc.enter_num()
        print('Enter the exponent')
        exponent = calc.enter_num()
        result = calc.exp(base,exponent)
        return result

    elif op == 7:
        print('Square Root')
        print('Enter a radicand: ')
        radicand = calc.enter_num()
        result = calc.square_root(radicand)
        return result

    elif op == 8:
        print('Inverse')
        num = calc.enter_num()
        result = calc.inv(num)
        return result

    elif op == 9:
        print('Sine')
        dr = int(input('Enter 1 for radians and 2 for degrees: '))
        if dr == 1:
            print('Enter an angle in radians to find Sin(angle): ')
            num = calc.enter_num()
            result = calc.sine(num)
            return result
        elif dr == 2:
            print('Enter an angle in degrees to find Sin(angle): ')
            num = calc.enter_num()
            result = calc.sine(math.degrees(num))
            return result

    elif op == 10:
        print('Cosine')
        dr = int(input('Enter 1 for radians and 2 for degrees: '))
        if dr == 1:
            print('Enter an angle in radians to find Cos(angle): ')
            num = calc.enter_num()
            result = calc.cosine(num)
            return result
        elif dr == 2:
            print('Enter an angle in degrees to find Cos(angle): ')
            num = calc.enter_num()
            result = calc.cosine(math.degrees(num))
            return result

    elif op == 11:
        print('Tangent')
        dr = int(input('Enter 1 for radians and 2 for degrees: '))
        if dr == 1:
            print('Enter an angle in radians to find Tan(angle): ')
            num = calc.enter_num()
            result = calc.tangent(num)
            return result
        elif dr == 2:
            print('Enter an angle in degrees to find Tan(angle): ')
            num = calc.enter_num()
            result = calc.tangent(math.degrees(num))
            return result

    elif op == 12:
        print('Switch Sign')
        print("Enter a number to change its sign: ")
        num = calc.enter_num()
        result = calc.switch_sign(num)
        return result

    elif op == 13:
        print('arcSin')
        dr = int(input('Enter 1 for radians and 2 for degrees: '))
        if dr == 1:
            print('Enter an angle in radians to find arcSin(angle): ')
            num = calc.enter_num()
            result = calc.invSin(num)
            return result
        elif dr == 2:
            print('Enter an angle in degrees to find arcSin(angle): ')
            num = calc.enter_num()
            result = calc.invSin(math.degrees(num))
            return result
        elif dr == 2:
            num = input('Enter an angle in degrees to find arcSin(angle): ')
            result = calc.invSin(math.degrees(num))
            return result

    elif op == 14:
        print('arcCos')
        dr = int(input('Enter 1 for radians and 2 for degrees: '))
        if dr == 1:
            print('Enter an angle in radians to find arcCos(angle): ')
            num = calc.enter_num()
            result = calc.invCos(num)
            return result
        elif dr == 2:
            print('Enter an angle in degrees to find arcCos(angle): ')
            num = enter_num()
            result = calc.invCos(math.degrees(num))
            return result
        elif dr == 2:
            num = input('Enter an angle in degrees to find arcCos(angle): ')
            result = calc.invCos(math.degrees(num))
            return result

    elif op == 15:
        print('arcTan')
        dr = int(input('Enter 1 for radians and 2 for degrees: '))
        if dr == 1:
            print('Enter an angle in radians to find arcTan(angle): ')
            num = calc.enter_num()
            result = calc.invTan(num)
            return result
        elif dr == 2:
            print('Enter an angle in degrees to find arcTan(angle): ')
            num = calc.enter_num()
            result = calc.invTan(math.degrees(num))
            return result
        elif dr == 2:
            num = input('Enter an angle in degrees to find arcTan(angle): ')
            result = calc.invTan(math.degrees(num))
            return result

    elif op == 16:
        print('Factorial')
        print('Enter a number to find its factorial: ')
        num = calc.enter_num()
        result = calc.factorial(num)
        return result

    elif op == 17:
        print('Log base 10')
        print('Enter a number to find its log with base 10: ')
        num = calc.enter_num()
        result = calc.log_base_10(num)
        return result

    elif op == 18:
        print('Inverse Log 10^x')
        print('Enter a number to find its inverse log with base 10: ')
        num = calc.enter_num()
        result = calc.inv_log_10(num)
        return result

    elif op == 19:
        print('Log base e, Ln')
        print('Enter a number to find its log with base e: ')
        num = calc.enter_num()
        result = calc.log_base_e(num)
        return result

    elif op == 20:
        print('Inverse log base e, e^x')
        print('Enter a number to find its inverse log with base e: ')
        num = calc.enter_num()
        result = calc.inv_log_e(num)
        return result

    elif op == 21:
        print(' Log of n base b')
        print('Enter a number: ')
        n = calc.enter_num()
        print('Enter a base: ')
        b = calc.enter_num()
        result = calc.log_base_y(n,b)
        return result

    elif op == 22:
        return 3.14159265359

    elif op == 23:
        return 6.02*(10**23)

    elif op == 24:
        rnum = randint(0,100)
        return rnum

    elif op == 25:
        memStore = float(input('Enter a value to store: '))
        print(memStore)
        return memStore

    elif op == 26:
        if type(memStore) != None:
            print(memStore)

    elif op == 27:
        store_choice = input('Do you want to clear memory? Y/N: ').lower()
        if store_choice == 'y':
            memStore = 0
        else:
            pass
        print(memStore)
        return memStore

    elif op == 28:
        condi = False
        print('Goodbye!')

#### Small Loop ####

def choose_small_op():
    print('1 Addition           2 Subtraction       3 Multiplication        4 Division')
    print('5 Square             6 Power             7 Square Root           8 Inverse')
    print('9 M+                 10 MRC              11 MC                   12 Exit')
    print(' ')
    op = int(input('Choose an operation: '))

    memStore = None

    if op == 1:
        print('Addition')
        print('Enter the second addend: ')
        addend2 = calc.enter_num()
        result = calc.add2(addend2)
        return result

    elif op == 2:
        print('Subtraction')
        print('Enter the subtrahend: ')
        subtrahend = calc.enter_num()
        result = calc.subtract2(subtrahend)
        return result

    elif op == 3:
        print('Multiplication')
        print('Enter the second factor: ')
        b = calc.enter_num()
        result = calc.multiply2(b)
        return result

    elif op == 4:
        print('Division')
        print('Enter the divisor: ')
        divisor = calc.enter_num()
        result = calc.divide2(divisor)
        return result

    elif op == 5:
        print('Square')
        result = calc.square2(main_result)
        return result

    elif op == 6:
        print('Power')
        print('Enter the exponent')
        exponent = calc.enter_num()
        result = calc.exp2(exponent)
        return result

    elif op == 7:
        print('Square Root')
        result = calc.square_root2(main_result)
        return result

    elif op == 8:
        print('Inverse')
        #num = enter_num()
        result = calc.inv2(main_result)
        return result

    elif op == 9:
        memStore = main_result
        print(memStore)
        return memStore

    elif op == 10:
        if type(memStore) != None:
            print(memStore)
        else:
            print('Empty')

    elif op == 11:
        store_choice = input('Do you want to clear memory? Y/N: ').lower()
        if store_choice == 'y':
            memStore = 0
        else:
            pass
        print(memStore)
        return memStore

    elif op == 12:
        condi = False
        print('Goodbye!')


calc = Calculator()

condi = True
while condi:
    main_result = choose_op()
    #print(f'Result: {main_result}')
    calc.choose_data_type()
    print('')
    cont = input('Continue with current value Y/N? \n'
                 'Warning: N clears the display: ').lower()
    print('')
    if cont == 'y':
        condi2 = True
        while condi2:
            main_result = choose_small_op()
            #print(f'Result: {main_result}')
            calc.choose_data_type()
            print('')
            cont2 = input('Continue with current value Y/N?\n'
                          'Warning: N clears the display: ').lower()
            print('')
            if cont2 == 'y':
                condi2 = True
            else:
                break

if __name__ == '__main__':
    main()
