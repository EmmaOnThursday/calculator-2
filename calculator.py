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
        #print len(tokens)
        try:
            num1 = int(tokens[1])
            if len(tokens) == 3:
                try:
                    num2 = int(tokens[2])
                    if tokens[0] == "+":
                        return add(num1, num2)
                    elif tokens[0] == "-":
                        return subtract(num1, num2)
                    elif tokens[0] == "*":
                        return multiply(num1, num2)
                    elif tokens[0] == "/":
                        return divide(num1, num2)
                    elif tokens[0] == "pow":
                        return power(num1, num2)
                    elif tokens[0] == "mod":
                        return mod(num1, num2)
                except (ValueError, NameError):
                    return "Please enter problem blah blah balh" #next thing we were gonna do was specific form message for user
            elif len(tokens) == 2:
                if tokens[0] == "square":
                    return square(num1)
                elif tokens[0] == "cube":
                    return cube(num1)
            elif tokens[0] == "q":
                break
            else:
                return "some error message here"
        except (ValueError, NameError):
            return "Please enter problem in the form [operand] plus [integer(s)]."
        

        
        
print calculator()