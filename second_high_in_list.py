# Python code to return the second high in a list
# Author: Binggang Liu

list = [3,0,10,9,6,2,-3]

most_high = None
second_high = None

for i in list:
    if most_high == None:
        most_high = i
    elif i > most_high:
        second_high = most_high
        most_high = i
    else:
        most_high = most_high
        if second_high == None:
            second_high = i
        elif i > second_high:
            second_high = i
        else:
            second_high = second_high

print("The second highest number in the list is ",  second_high)
