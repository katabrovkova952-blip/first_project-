def first_word(text):
    """Пошук першого слова"""
    text_new = text.replace(".", " ").replace(",", " ").split()
    if text_new:
        return text_new[0]
    raise ValueError("Текст не може бути порожнім")

assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')
