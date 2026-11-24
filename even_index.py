word = input("Enter a word: ")

print("Characters at even positions:")

for character in range(0, len(word), 2):

    print(word[character], end="-")
