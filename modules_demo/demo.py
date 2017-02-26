from modules_demo.math_lib import *;
# from a import b
# import a and then call a.add_two_numbers()

if __name__ == '__main__':
    raw_input = input('Please enter two numbers seperated by space')
    while(True):
        firstNumber, secondNumber = raw_input.split(' ');
        choice = int(input('Please enter \n 1 to add \n 2 to multiply \n 3 to divide \n 4 to subtract'))
        if choice == 1:
            print(add_two_numbers(firstNumber, secondNumber))
        elif choice == 2:
            print(multiply_two_numbers(firstNumber, secondNumber))
        elif choice == 3:
            print(divide_two_numbers(firstNumber, secondNumber))
        elif choice == 4:
            print(subtract_two_numbers(firstNumber, secondNumber))
        else:
            print('Incorrect Choice')
