# Python codes for creating a class and instantiate objects using class
# Author Binggang Liu

#The Commented lines below demonstrate an example of a basic Python class.
#Followed by codes for a more standard python class example.

'''
class Dog:
    sound = "Woof woof"
    running = "Dog run"

    def bark(self):
        print(self.sound)

    def run(self):
        print(self.running)

def main():
    murphy = Dog()
    murphy.bark()
    murphy.run()

if __name__ == '__main__':
    main()
'''

class MyDog(object):

    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

#        super(MyDog, self).__init__()
#        self.arg = arg

    def show_name(self):
        print("Dog " + self.name)

dog1 = MyDog("Murphy", "Brown with White", 58)
dog2 = MyDog("Apple", "Black", 39)

dog1.show_name()
print("--Color: ", dog1.color)
print("--Weight(lb): ", dog1.weight)

dog2.show_name()
print("--Color: ", dog2.color)
print("--Weight(lb): ", dog2.weight)
