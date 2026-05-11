import string
text = input("Enter a string: ").title()
result = "#"
for _ in text:
    if _ not in string.punctuation and _ != " ":
        result += _
result = result[:140]
print(result)
