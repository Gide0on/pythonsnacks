word = input("Enter a word: ")

vowelCount = 0
consonantCount = 0

for letter in word.lower():

    if letter in "aeiou":
        vowelCount += 1

    elif letter in "bcdfghjklmnpqrstvwxyz":
        consonantCount += 1

print("Number of vowels:", vowelCount)
print("Number of consonants:", consonantCount)
