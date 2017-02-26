# we will be defining some useless functions in this module

def doSomething(a, b, c):
    print(a, b, c)

def doSomethingWithDefaultArgs(a=1, b=2, c=None):
    print(a, b, c)

# How are arguments passed to function? By Value? By reference? By copy of reference?

def function(a):
    a = 10;
    print ('a:'+ str(a))

def function2(a):
    a.append(100)

# Using class

class A:

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return 'value:'+ str(self.value)

def assignNewValue(obj, newValue):
    obj.value = newValue;


if __name__ == '__main__':
    doSomething(3, 3, 3)
    doSomethingWithDefaultArgs()

    # b = 20
    # print(b)
    # function(b)
    # print(b)
    #
    # b = [1, 2]
    # print(b)
    # function(b)
    # print(b)
    #
    # b = [1, 2]
    # print(b)
    # function2(b)
    # print(b)


    item = A(1)
    print(item)
    assignNewValue(item, 20)
    print(item)
