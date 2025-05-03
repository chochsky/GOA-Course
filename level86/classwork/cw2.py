def remove_digits(text):
    result = ""
    for char in text:
        if not char.isdigit():
            result += char
    return result

# მაგალითი:
print(remove_digits("ale4qs6and3re"))  # aleqsandre
