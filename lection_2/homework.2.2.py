a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
average = (a + b + c) / 3
print("Average: ", average)

numbers = input("Enter your three numbers: ")
a, b, c = map(float, numbers.split(","))     # map(float, ...) = перетворює все в числа.
                                    # split() = розбиває строку "2, 4, 6" в список ["2", " 4", " 6"]
average = (a + b + c) / 3
print(average)