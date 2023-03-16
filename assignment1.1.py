import math

print("calculator")
print("this calculator operations are :")
print(" + : sum ")
print(" - : sub ")
print(" * : mul ")
print(" / : div ")
print("sqrt")
print("sin")
print("cos")
print("tan")
print("cot")
print("factorial")
print("please choose your operation: cos") 

op = input("operation:")

if op == "+" or op == "-" or op == "*" or op == "/":
    a = float(input("please enter first number: "))
    b = float(input("please enter second number: "))
else:
    a = float(input("please enter the number: "))

if op == "+":
    result = a + b 

elif op == "-":
    result = a - b 

elif op == "*":
    result = a * b 

elif op == "/":
    result = a / b

elif op == "sqrt":
    result = math.sqrt(a)

elif op == "sin":
    result = math.sin(a)

elif op == "cos":
    result = math.cos(a)

elif op == "tan":
    result = math.tan(a)

elif op == "cot":
    result = math.tanh(a)

elif op == "factorial":
    result = math.factorial(a)

print(result)    
if op == "sin" or op == "cos" or op == "tan" or op == "cot":
    print("and the degree is: ", math.degrees(a))