"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


def calculator():
    while True:
        input = raw_input(">") #get input from user here
        tokens = input.split(" ")

        try:
            num1 = int(tokens[1])

        except (ValueError, NameError):
            print "Please enter problem in the form [operand] plus [integer(s)]."
        

        if len(tokens) == 3:
            try:
                num2 = int(tokens[2])
            except (ValueError, NameError):
                print "Please enter problem blah blah balh" #next thing we were gonna do was specific form message for user
            if tokens[0] == "+":
                return add(num1, tokens[2])
            elif tokens[0] == "-":
                return subtract(num1, tokens[2])
            elif tokens[0] == "*":
                return multiply(num1, tokens[2])
            elif tokens[0] == "/":
                return divide(num1, tokens[2])#insert add, multiply, subtract, divide, power, mod here
            elif tokens[0] == "pow":
                return power(tokens[1], tokens[2])
            elif tokens[0] == "mod":
                return mod(tokens[1], tokens[2])

        elif len(tokens) == 2:
            if tokens[0] == "square":
                return square(tokens[1])
            elif tokens[0] == "cube":
                return cube(tokens[1])#insert square, cube

        elif tokens[0] == "q":
            break
        else:
            return "some error message here"

        
        
        else:
            return "I do not understand your input, please try again"


calculator()