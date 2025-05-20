words = ["banana", "apple", "pear"]
sorted(words)  # ['apple', 'banana', 'pear']
sorted(words, key=len)  # ['pear', 'apple', 'banana']
sorted(words, reverse=True)  # ['pear', 'banana', 'apple']
