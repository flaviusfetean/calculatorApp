from operations import add, subtract, divide

print("Simple Calculator")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

op = input("Enter operation (+,-,*,/): ")

if op == '+':
    print(add(a, b))
elif op == '-':
    print(subtract(a, b))
elif op == '/':
    print(divide(a, b))
else:
    print("Invalid operation")
