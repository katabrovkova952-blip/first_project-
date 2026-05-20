def add_one(some_list):
    result = []
    res = 0
    for i in some_list:
        res = res * 10 + i
    res += 1
    for j in str(res):
        result.append(int(j))
    return result

assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")
