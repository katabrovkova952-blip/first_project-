def popular_words (text, words):
    result = {}
    new_text = text.lower().split()
    for i in new_text:
        if i in words:
            result[i] = result.get(i, 0)+1
    for j in words:
        if j not in new_text:
            result[j] = result.get(j, 0)
    return result

assert popular_words('''When I was One I had just begun 
When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')

