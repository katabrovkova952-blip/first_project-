a = float(input("Enter a number a: "))
action = input("Enter an action: ")
b = float(input("Enter a number b: "))
if action == "-":
    print("Result:", a - b)
elif action == "+":
    print("Result:", a + b)
elif action == "*":
    print("Result:", a * b)
elif action == "/":
    if b == 0:
        print("Error")
    else:
        print("Result:", a / b)