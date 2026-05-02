# num = [1, 2, 3, 4, 5, 6]
# num = [1, 2, 3]
# num = [1, 2, 3, 4, 5]
# num = [1]
num = []
if len(num) % 2 != 0:
    y = len(num) // 2
    y = [num[:y+1]] + [num[y+1:]]
    print(y)
elif len(num) % 2 == 0:
    y = len(num) // 2
    y = [num[:y]] + [num[y:]]
    print(y)
