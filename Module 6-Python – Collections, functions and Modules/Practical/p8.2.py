# Write a Python program to create a calculator using functions.

def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    return a / b

choice =int(input("Enter your choice "))

x=float(input("Enter first number"))
y=float(input("Enter second number"))

if choice ==1:
    print("Result =",add(x,y))
elif choice ==2:
    print("Result =",sub(x,y))
elif choice ==3:
    print("Result =",mul(x,y))
elif choice ==4:
    print("Result =",div(x,y)) 
else:
    print("Invalid choice")               