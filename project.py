#Input value
sign = input("Operator: ") #The operator
a = int(input("a's value: "))
b = int(input("b's value: "))

#Function of the specific operators.

def func_add(a,b):
    return a + b
def func_sub(a,d):
    return a - b
def func_mult(a,b):
    return a * b
def func_div(a,b):
    return a / b
def func_expo(a,b):
    return a ** b

#Assigns a sign to a function
#Calls the functions
#Prints the functions
if sign == '+':
    print(f"Total: {func_add(a,b)}")
elif sign == '-':
    print(f"Total: {func_sub(a,b)}")
elif sign == '*':
    print(f"Total: {func_mult(a,b)}")
elif sign == '/' :
    print(f"Total: {func_div(a,b)}")
elif sign == '**':
    print(f"Total: {func_expo(a,b)}")
else:
    print("Error")
