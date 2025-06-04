words = []

while True:
    word = input("შეიყვანე სიტყვა (ან დაწერე 'საკმარისია' დასასრულებლად): ")
    if word.lower() == 'საკმარისია':
        break
    words.append(word)
sorted_words = sorted(words, key=len)

print("დასორტირებული სია (სიმბოლოების რაოდენობით):")
print(sorted_words)
