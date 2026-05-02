num = [12, 3, 4, 10]
# num = [1]
# num = []
# num = [12, 3, 4, 10, 8]
if len(num) > 1:
    y = num.pop(-1)
    num.insert(0,y)
    print(num)
else:
    print(num)