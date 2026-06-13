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

# def draw_rectangle(w, h, fill):
#     for i in range(w):
#         for j in range(h):
#             print(fill, end="")
#         print()
#     return
#
# dct = {"fill": "#", "w": 5, "h": 8, 'j': 234}
# draw_rectangle(**dct)

# def find_gcd(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a
# print(find_gcd(45, 30))

# def add_decorator(number):
#     """
#     Реалізує декоратор, який змінює поведінку функції, додаючи до результату функції число.
#
#     :param number: Число для додавання.
#     :return: Декоратор для додавання числа до результату функції.
#     """
#     def decorator(func):
#        def wrapper(*args, **kwargs):
#            res = func(*args, **kwargs)
#            return res + number
#        return wrapper
#     return decorator
#
# @add_decorator(5)
# def example_function(x):
#     return x * 2
#
# @add_decorator(7)
# def summer(x):
#     return x + 10
#
# # Перевірка
# print(example_function(2))
# print(summer(5))
# assert example_function(2) == 9

# def repeat_decorator(repeat_count):
#     def counter(func):
#         def wrapper(*args, **kwargs):
#             for i in range(repeat_count):
#                 func(*args, **kwargs)
#         return wrapper
#     return counter
#
# @repeat_decorator(3)
# def example_function():
#     print("Function called")
#
# @repeat_decorator(5)
# def sumar(x, y):
#     print(x + y)
#
# example_function()
# sumar(1, 2)
#
# workers = {}
#
# def link(address=None):
#     def add_worker(func):
#         workers[address] = func
#         def get_answer(*args, **kwargs):
#             return str(func(*args, **kwargs))
#         return get_answer
#     return add_worker
#
# @link("\\main")
# def main_page():
#     return "Hello word page"
#
# @link("\\main\\goods")
# def get_goods(list_goods):
#     return list_goods
#
# print(workers)

# def cache(func):
#     dct = {}
#     def wrapper(*number, **kwargs):
#         key = (number, tuple(kwargs.items()))
#         if key in dct:
#             return dct[key]
#         else:
#             res = func(*number, **kwargs)
#             dct[key] = res
#             return res
#     return wrapper
#
# @lru_cache
# def square(x, y):
#     print("Обчислюю...")
#     return (x + y) ** 2
#
# print(square(5, y= 3))
# print(square(5, y= 2))

# def retry(x):
#     def deco(func):
#         def wrapper():
#             for i in range(1, x + 1):
#                 try:
#                     return func()
#                 except ValueError:
#                     print(f"Спроба {i}")
#
#             print("Усі спроби вичерпано")
#         return wrapper
#     return deco
#
# @retry(3)
# def test():
#     raise ValueError
# test()

# def create_dictionary(*args):
#     dct = {}
#     for index, i in enumerate(args):
#         if not isinstance(i, (list, dict, set)):
#             dct[i] = index
#         else:
#             print(f"Cannot add {i} to the dict!")
#     return dct
# print(create_dictionary("rt", 23, 34.5, {}, [], 23))

# def binary_search(arr, target):
#     left = 0
#     right = len(arr) - 1
#     while left <= right:
#         middle = (left + right) // 2index = int(input("Input index "))
#         value = arr[middle]
#         if value == target:
#             return middle
#         elif value < target:
#             left = middle + 1
#         else:
#             right = middle - 1
#     return -1
#
# assert binary_search([11, 12, 22, 25, 34, 64, 90, 100, 130, 140 ,200], 1320) == -1

