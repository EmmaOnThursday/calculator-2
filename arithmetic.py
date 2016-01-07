def add(*args):
    return sum(args)

def subtract(*args):
    #read list of arguments
    product = args[0] #product = 5
    for x in range(1,len(args)): #for any number in the range (1-5)
        product -= args[x]
    return product

def multiply(*args):
    product = args[0]
    for x in range(1, len(args)):
        product = product * args[x]
    return product 

def divide(*args):
    product = args[0]
    for x in range(1, len(args)):
        product = product / args[x]
    return product

def square(num1):
    return num1 ** 2 

def cube(num1):
    return num1 ** 3

def power(num1, num2):
    return num1 ** num2

def mod(num1, num2):
    return num1 % num2

#print multiply(4,2,1)