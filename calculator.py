import time
# Simple Terminal calculator using functions

def add(x, y):
    sum = x + y
    equation = "{num_one} + {num_two} = {sum}".format(num_one=x, num_two=y, sum=sum)
    print(equation)
def subtract(x, y):
    diff = x - y
    equation = "{num_one} - {num_two} = {difference}".format(num_one=x, num_two=y, difference=diff)
    print(equation)
def multiply(x, y):
    mul = x * y
    equation = "{num_one} x {num_two} = {multiple}".format(num_one=x, num_two=y, multiple=mul)
    print(equation)
def divide(x, y):
    div = x / y
    equation = "{num_one} / {num_two} = {division}".format(num_one=x, num_two=y, division=div)
    print(equation)
def power(x, y): # power rules
    pow = x ** y
    equation = "{num_one}^{num_two} = {powers}".format(num_one=x, num_two=y, powers=pow)
    print(equation)
def root(x, y): # Roots: square root, cube root, etc.
    roots = x ** (1 / y)
    equation = "{num_one}^(1/{num_two}) = {root}".format(num_one=x, num_two=y, root=roots)
    print(equation)


while True:
    question = input("What operation do you want use? Addition, subtraction, multiplication, division, power, or root? ")

    if (question.lower() == "addition"):
        num_one = int(input("Enter your first number: "))
        num_two = int(input("Enter your second number: "))
        add(num_one, num_two)
    elif (question.lower() == "subtraction"):
        num_one = int(input("Enter your first number: "))
        num_two = int(input("Enter your second number: "))
        subtract(num_one, num_two)
    elif (question.lower() == "multiplication"):
        num_one = int(input("Enter your first number: "))
        num_two = int(input("Enter your second number: "))
        multiply(num_one, num_two)
    elif (question.lower() == "division"):
        num_one = int(input("Enter your first number: "))
        num_two = int(input("Enter your second number: "))
        divide(num_one, num_two)
    elif (question.lower() == "power"):
        num_one = int(input("Enter your first number: "))
        num_two = int(input("Enter your second number: "))
        power(num_one, num_two)
    elif (question.lower() == "root"):
        num_one = int(input("Enter your first number: "))
        root_index = int(input("What do you want the index to be (the index for square root would be 2, cube root would be 3, etc.)? "))
        root(num_one, root_index)
    else:
        print("Enter a valid operation")
        break

    # Next calculation
    next = input("Do you want to do another calculation? type 'yes' or 'no' ")
    if next.lower() == "no":
        print("Ending Calculator...")
        time.sleep(3)
        break


