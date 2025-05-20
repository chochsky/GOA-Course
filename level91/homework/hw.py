words = []

while True:
    word = input("შეიყვანე სიტყვა (თუ საკმარისია, აკრიფე 'საკმარისია'): ")
    if word == "საკმარისია":
        break
    words.append(word)
sorted_words = sorted(words, key=len)

print("დასორტირებული სია (სიმბოლოების რაოდენობით):")
print(sorted_words)
