import string
text = input("Enter a text: ").split("-")
text_1 = text[0]
text_2 = text[1]
index_1 = string.ascii_letters.index(text_1)
index_2 = string.ascii_letters.index(text_2)
result = string.ascii_letters[index_1:index_2 +1]
print(result)

# abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ

