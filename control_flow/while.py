# Without recursion

def factorial(i):
    result = 1
    while i != 1:
        result = result*i
        i -= 1

    return result

def factorial_using_for_loop(number):
    result = 1
    for i in range(1, number+1):
        result *= i

    return result

if __name__ == '__main__':
    rawInput = input('Please enter a number\n')
    number = int(rawInput)
    print('\nThis is using while loop:')
    print(factorial(number))
    print("This is for loop")
    print(factorial_using_for_loop(number))