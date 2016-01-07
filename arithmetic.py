def add(*args):
    print args[0]
    return sum(args[0])

def subtract(*args):
    #changes tuple to a list
    product = args[0][0]
    for x in range(1,len(args[0])):
        product -= args[0][x]
    return product

def multiply(*args):
    product = args[0]
    for x in range(1, len(args[0])):
        product = product * args[0][x]
    return product 

def divide(*args):
    product = args[0][0]
    for x in range(1, len(args[0])):
        product = product / args[0][x]
    return product

def square(num1):
    return num1 ** 2 

def cube(num1):
    return num1 ** 3

def power(num1, num2):
    return num1 ** num2

def mod(num1, num2):
    return num1 % num2
