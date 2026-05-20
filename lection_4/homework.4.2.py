# numbers = [0, 1, 7, 2, 4, 8]
# numbers = [6]
numbers = [0]

print(sum(numbers[::2]) * numbers[-1] if numbers else 0)