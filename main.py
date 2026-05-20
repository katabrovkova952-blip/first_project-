# number = int(input("Enter a number: "))
# while number >= 9:
#     result = 1
#     while number > 0:
#         digit = number % 10 або через divmod
#         result *= digit
#         number //= 10
#     number = result
# print(number)

# x = {1: "one", 2: "two"}
# y = {"name":{"Anna": 19, "Kate": 20}}
# x.update(y)
# x["name"].update({"Max": 18, "Kate": 30, "Anna": 50})
# print(x)

# from dataclasses import dataclass
# @dataclass
# class Person:
#     name: str
#     age: int
# p = Person("Alex", 19)
# print(p)
# print(type(p))
# print(isinstance(p, int)

# res = []
# mountain = [
#     [7],
#     [5, 8],
#     [9, 8, 2],
#     [1, 3, 5, 6],
#     [6, 2, 4, 4, 5],
#     [9, 5, 3, 5, 5, 7],
#     [7, 4, 6, 4, 7, 6, 8]]
# def can_go(i):
#     max_res = sum(max(i))
#     return i

# animals = [
#     {"name": "cat", "type": "pet", "legs": 4},
#     {"name": "dog", "type": "pet", "legs": 4},
#     {"name": "spider", "type": "wild", "legs": 8},
#     {"name": "chicken", "type": "farm", "legs": 2},
# ]
# def filter_animals(animals, **filters):
#     result = []
#     for i in animals:
#         match = True
#         for key, value in filters.items():
#             if i.get(key) != value:
#                 match = False
#                 break
#         if match:
#             result.append(i)
#     return result
#
# print(filter_animals(animals, legs=4))

def draw_rectangle(w, h, fill):
    for i in range(w):
        for j in range(h):
            print(fill, end="")
        print()
    return

dct = {"fill": "#", "w": 5, "h": 8, 'j': 234}
draw_rectangle(**dct)