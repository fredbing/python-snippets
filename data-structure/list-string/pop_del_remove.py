
'''
comparing list methods: pop(), del(), remove()
'''

fruits = ['Apple', 'Banana', 'Cherry', 'Durian', 'Elderberry', 'Fig', 'Grape']

'''
#pop(), pops out the last element each time
#fruits becomes an empty list in the end
for i in range(len(fruits)):
    print(i)
    fruits.pop()
    print(fruits)


#del(), deletes element by index
#for each loop, when an element with index i is deleted, the original fruits list is modified and reduced length by one element,
# and in the next loop, the index of each of the remaining elemets is reduced by one. Hence del() will skip one element starting at the second loop.
# in the end, the fruits list still have ['Banana', 'Durian', 'Fig']
for i in range(len(fruits)):
    print(i)
    del fruits[i]
    print(fruits)

'''

#remove(), deletes element by value
#for each loop, when an element removed, similar to del() menthod, the original fruits list is modified and reduced by one element,
# and in the next loop, the index of each of the remaining elemets is reduced by one. remove() will slao skip one element starting at the second loop.
# in the end, the fruits list still have ['Banana', 'Durian', 'Fig']
for fruit in fruits:
    print(fruit)
    fruits.remove(fruit)
    print(fruits)
