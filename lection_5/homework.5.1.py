import string
import keyword
text = input("Enter a text: ")
punkt = string.punctuation.replace('_', ' ')

result = True

if text[0] in string.digits:
    result = False
elif text in keyword.kwlist:
    result = False
elif any(i in punkt for i in text):
    result = False
elif any(i.isupper() for i in text):
    result = False
elif text.count("_") != 1 and text.count("_") == len(text):
    result = False
print(result)

