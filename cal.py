def calculator(a, b):
    print("addition",a+b)
    print("substraction",a-b)
    print("multiplication",a*b)
    if b != 0:
        print("division",a/b)
    else:
        print("division: error (division by zero)")

#example
num1 = float(input("enter first number:"))
num2 = float(input("enter second number:"))

calculator(num1, num2)