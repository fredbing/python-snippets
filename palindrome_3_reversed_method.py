# Python code to test if a word is palindrome
# by checking if every letter is same as in its reverse word
# with the reversed() method to reverse a list (a string is considered a list)
# Author: Binggang Liu


word = input("Enter the word: ")

reverse_word = ''.join(reversed(word))

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
