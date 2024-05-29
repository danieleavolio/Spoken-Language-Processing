from num2words import num2words
def convert_text(text):

    words = text.split()
    result = ''
    for word in words:
        if word.isnumeric():
            result += num2words(int(word)) + ' '
        else:
            result += word + ' '

    return result

text = 'I have 42 apples and 1000 bananas'
print(convert_text(text))

