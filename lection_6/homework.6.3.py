number = int(input("Enter a number: "))
while number >= 9:
    result = 1
    while number > 0:
        digit = number % 10
        result *= digit
        number //= 10
    result = number
print(number)