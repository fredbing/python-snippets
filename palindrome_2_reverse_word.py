# Python code to test if a word is palindrome
# by checking if every letter is same as in its reverse word
# Author: Binggang Liu


word = input("Enter the word: ")

reverse_word = word[::-1]

check = 0

for i in range(len(word)):
    if word[i] == reverse_word[i]:
        check += 0
    else:
        check += -10

if check == 0:
    print("Yes, this word is a palindrome!")

else:
    print("No, this word is not a palindrome")
