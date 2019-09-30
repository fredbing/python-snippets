# Python code to test if a word is palindrome
# Author: Binggang Liu

import math

word = input("Enter the word: ")

check = 0

for i in range(math.floor((len(word))/2)):
    if word[i] == word[-1-i]:
        check += 0
    else:
        check += -10

if check == 0:
    print("Yes, this word is a palindrome!")

else:
    print("No, this word is not a palindrome")
