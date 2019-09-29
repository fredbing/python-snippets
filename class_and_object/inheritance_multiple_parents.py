'''
multiple inheritance (multiple parent classes)

Author: Binggang Liu
'''

# In python3, Class Product is equivalent to Class Product(object)


class Animal(object):

    # Constructor
    def __init__(self, movement):
        self.movement = movement


class Pet(object):

    def __init__(self, genus):
        self.genus = genus


class Dog(Animal, Pet):
    def __init__(self, movement, genus, isMale):
        Animal.__init__(self, movement)
        Pet.__init__(self, genus)

        self.isMale = isMale


murphy = Dog('Running', 'Canis', True)

print("The type of movement of this animal makes: ", murphy.movement)

print("The genus of this animal: ", murphy.genus)

print("Is this animal a male? ", murphy.isMale)
