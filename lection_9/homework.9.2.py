def difference(*numbers):
    res = 0
    if numbers:
        max_number = max(numbers)
        min_number = min(numbers)
        res = max_number - min_number
    return round(res, 2)

assert difference(1, 2, 3) == 2, "Test1"
assert difference(5, -5) == 10, "Test2"
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, "Test3"
assert difference() == 0, "Test4"
print("OK")
