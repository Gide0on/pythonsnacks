word = input("Enter a word: ")

reversedWord = ""

for letter in word:
    reversedWord = letter + reversedWord

if word.lower() == reversedWord.lower():
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")
