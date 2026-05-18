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
# print(isinstance(p, int))
