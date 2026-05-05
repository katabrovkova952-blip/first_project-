# def click():
#     print("Hello")
# click()

# def add(c, f):
#     return c % f
# print(add(10,5))

# def double(n):
#     return n * 2
# x = double(3)
# y = double(5)
# print(x + y)

# numbers = [5, 10, 3, 7]
# total = 0
# for number in numbers:
#     total += number
# print(total)

# numbers = [8, 2, 15, 4 , 9]
# max_num = numbers[0]
# for num in numbers:
#     if num > max_num:
#         max_num = num
# print(max_num)

# numbers = [12, 4, 8, 1, 9]
# max_num = numbers[0]
# min_num = numbers[0]
# for num in numbers:
#     if num > max_num:
#         max_num = num
#
#     if num < min_num:
#         min_num = num
# print("Max:", max_num)
# print("Min:", min_num)

# numbers = []
# while True:
#     value = input(Enter your number:)
#
#     if value == "stop":
#         break
#
#     number = int(value)
#     numbers.append(number)
#
# total = 0
# for num in numbers:
#     total += num
#
# print("Numbers:", numbers)
# print("Total:", total)

# numbers = [7, 3, 12, 1, 9]
# min_number = numbers[0]
# max_number = numbers[0]
#
# def square(n):
#     return n * n
# print(square(4))
# print(square(6))

# numbers = [2, 5, 8, 3]
# for num in numbers:
#     if num > 4:
#       print(num*2)

# def get_max(numbers):
#     max_number = numbers[0]
#     for num in numbers:
#          if num > max_number:
#              max_number = num
#
#     return max(numbers)
#
# print(get_max([12, 9, 2, 9, 589, 1009]))

# numbers = []
# total = 0
# while True:
#     value = input("Enter a numbers:")
#     if value == "stop":
#         break
#     number = int(value)
#     numbers.append(number)
#
# min_num = numbers[0]
# max_num = numbers[0]
# for num in numbers:
#         total += num
#         if num > max_num:
#             max_num = num
#
#         if num < min_num:
#            min_num = num
# print(numbers)
# print(total)
# print(min_num)
# print(max_num)
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# city = input("Enter your city: ")
# user = {
#     "name": name,
#     "age": age,
#     "city": city
# }
# for key, value in user.items():
#     print(key, value)

# number = float(input("Enter a number: "))
# res = number.is_integer()
# x = bin(int(number))
# a = hex(int(number))
# b = oct(int(number))
# rounded = round(number, 2)
#
# print("Is integer: ", res)
# print("Binary: ", x)
# print("Hex: ", a)
# print("Oct: ", b)
# print("Rounded: ", rounded)
# print("Ratio: ", number.as_integer_ratio())

# numbers = list(map(int, input("Enter a numbers: ").split(",")))
# max_number = numbers[0]
# max_index = 0
# for i in range(len(numbers)):
#     if numbers[i] > max_number:
#         max_number = numbers[i]
#         max_index = i
# print(max_number)
# print(max_index)

# number = int(input("Enter number: "))
#
# original = number
#
# # 1. Збираємо всі парні цифри у перевернутому порядку
# even_digits = 0
#
# temp = number
# while temp > 0:
#     temp, digit = divmod(temp, 10)
#
#     if digit % 2 == 0:
#         even_digits = even_digits * 10 + digit
#
# # 2. Збираємо нове число, замінюючи парні цифри
# new_number_reversed = 0
#
# temp = original
# while temp > 0:
#     temp, digit = divmod(temp, 10)
#
#     if digit % 2 == 0:
#         new_digit = even_digits % 10
#         even_digits //= 10
#     else:
#         new_digit = digit
#
#     new_number_reversed = new_number_reversed * 10 + new_digit
#
# # 3. Перевертаємо назад, бо збирали справа наліво
# result = 0
#
# while new_number_reversed > 0:
#     new_number_reversed, digit = divmod(new_number_reversed, 10)
#     result = result * 10 + digit
# print(result)

# num = [1, 2, 3, 4, 5, 6]
# num = [1, 2, 3, 4, 5]
# num = [1]
# num = []
# y = (len(num) + 1) // 2
# print([num[:y]] + [num[y:]])
#
# text = input("Enter a text:")
# retr = text[::-1]
# num = []
# for i in retr:
#     if i not in num:
#         num.append(i)
# print("".join(num))

# lst_1 = [10, 1, 10]
# max_value = max(lst_1)
# new_lst = []
# for num in lst_1:
#     if num < max_value:
#         new_lst.append(num)
#
# if new_lst:
#     max_value_two = max(new_lst)
#     print(max_value_two)
# else:
#     print("Don`t have second max")

# text = input("Enter your text: ").lower()
# vowels = "aeiou"
# count = 0
# for letter in text:
#     if letter in vowels:
#         count +=1
# print(count)








