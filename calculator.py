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
        print tokens
        if tokens[0] == "q":
            break
        else:
            try:
                arguments = []
                for num in tokens[1:]:
                    arguments.append(float(num))
                num1 = float(tokens[1])
                if tokens[0] == "+":
                    answer = add(arguments)
                elif tokens[0] == "-":
                    answer = subtract(arguments)
                elif tokens[0] == "*":
                    answer = multiply(arguments)
                elif tokens[0] == "/":
                    answer = divide(arguments)
                elif tokens[0] == "pow":
                    answer =  power(num1, num2)
                elif tokens[0] == "mod":
                    answer =  mod(num1, num2)
                elif tokens[0] == "square":
                    answer =  square(num1)
                elif tokens[0] == "cube":
                    answer =  cube(num1)
                else: 
                    answer = "something something"
            except (ValueError, NameError):
                    answer =  "Error: non-integers entered."
        print answer


        
        
calculator()