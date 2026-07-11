# from typing import Callable
#
#
# from functools import wraps
#
#
# def cache(func: Callable) -> Callable:
#     dct = {}
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         key = (args, tuple(kwargs.items()))
#         if key in dct:
#             print("Getting from cache")
#             return dct[key]
#         else:
#             print("Calculating new result")
#             value = func(*args, **kwargs)
#             dct[key] = value
#             return value
#     return wrapper
#
#
# @cache
# def add(a, b):
#     print("Start")
#     return a + b

# from collections import defaultdict
#
# def group_anagrams(words: list) -> list:
#     lst = defaultdict(list)
#     for word in words:
#         res = "".join(sorted(word))
#         lst[res].append(word)
#
#     return list(lst.values())
#
# print(group_anagrams([""]))

#
# class Cat:
#     def __init__(self, _name, age):
#         self.__name = _name   # захищене поле
#         self.age = age
#
#     def get_name(self): # Метод для читання
#         print("call get name")
#         return self.__name
#
#     def set_name(self, name_value): # Метод для запису
#         print("call set name")
#         self.__name = name_value
#
#     def del_name(self): # Метод видалення
#         print("call remove name")
#         del self.__name
#
#     # Створення властивості name
#     name = property(get_name, set_name)
#
#     def __str__(self):
#         msg = "Cat [ name = {}, age = {}]"
#         return msg.format(self.name, self.age, self.del_name)
#
# cat1 = Cat("Vaska", 6)
# cat1.name = "Barsic"
# print(Cat.name.fdel)
# print(cat1.name)
# print(cat1)


# class User:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, value):
#         self.__name = value
#
#     @name.deleter
#     def name(self):
#         del self.__name
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, value):
#         if value < 0:
#             raise ValueError("Вік не може бути від'ємним")
#         self.__age = value
#
#     @age.deleter
#     def age(self):
#         del self.__age
#
#     def __str__(self):
#         return f"User: {self.__name}, age: {self.__age}"
#
# user = User("Kate", 18)
#
# print(user.name)
# user.name = "Lora"
