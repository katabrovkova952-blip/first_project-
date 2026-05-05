numbers = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
# numbers = [0, 1, 0, 12, 3]
# numbers = [1, 0, 13, 0, 0, 0, 5]
# numbers = [0]
for num in numbers:
    if num == 0:
        numbers.remove(num)
        numbers.append(num)
print(numbers)
