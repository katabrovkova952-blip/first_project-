import string
def is_palindrome(text):
    text_1 = ''
    for i in text:
        if i in string.ascii_letters or i in string.digits:
            text_1 += i.upper()
    return text_1 == text_1[::-1]

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
