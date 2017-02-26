# Demonstrate if else using factorial(recursion)

def factorial_using_if_else(i):
    if i == 1:
        return 1
    else:
        return i*factorial_using_if_else(i-1)


if __name__ == '__main__':
    input = int(input('Please enter a number\n'))
    print(factorial_using_if_else(input))