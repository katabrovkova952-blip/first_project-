import string
import keyword
text = input("Enter a text: ")
result = True
if text[0] in string.digits:
    result = False
elif text in keyword.kwlist:
    result = False
elif "__" in text:
    result = False
else:
    for i in text:
        if i == "_":
            continue
        elif i in string.ascii_uppercase:
            result = False
            break
        elif i in string.punctuation or i == " ":
            result = False
            break
print(result)