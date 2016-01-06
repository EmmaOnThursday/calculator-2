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
        if tokens[0] == "q":
            break
        else:
            try:
                num1 = int(tokens[1])
                if len(tokens) == 3:
                    try:
                        num2 = int(tokens[2])
                        if tokens[0] == "+":
                            answer = add(num1, num2)
                        elif tokens[0] == "-":
                            answer = subtract(num1, num2)
                        elif tokens[0] == "*":
                            answer = multiply(num1, num2)
                        elif tokens[0] == "/":
                            answer = divide(num1, num2)
                        elif tokens[0] == "pow":
                            answer =  power(num1, num2)
                        elif tokens[0] == "mod":
                            answer =  mod(num1, num2)
                    except (ValueError, NameError):
                        answer =  "Please enter problem in the form [operand] plus [integer(s)]."
                elif len(tokens) == 2:
                    if tokens[0] == "square":
                        answer =  square(num1)
                    elif tokens[0] == "cube":
                        answer =  cube(num1)
                else:
                    answer = "Please enter a problem in the form of [operand] plus [integer(s)]."
            except (ValueError, NameError):
                answer =  "Please enter problem in the form [operand] plus [integer(s)]."
        print answer


        
        
calculator()