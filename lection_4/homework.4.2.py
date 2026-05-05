# numbers = [0, 1, 7, 2, 4, 8]
# numbers = [6]
numbers = [0]
if numbers == []:
    print(0)
else:
    print(sum(numbers[::2]) * numbers[-1])