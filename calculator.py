from operations import add, subtract

print("Simple Calculator")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

op = input("Enter operation (+,-,*,/): ")

if op == '+':
    print(add(a, b))
elif op == '-':
    print(subtract(a, b))
else:
    print("Invalid operation")
