'''
multi-level inheritance:
Author: Binggang Liu
'''

# In python3, Class Product is equivalent to Class Product(object)


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def getProductName(self):
        return self.name

    def getProductPrice(self):
        return self.price


class Food(Product):
    def __init__(self, name, price, isHealthy):
        #Product.__init__(self, name, price)
        super().__init__(name, price)
        # As shown above, there are two ways to inherit. By using super() function, there is no need
        #  to use the name of the parent class, in addition, "self" is not required to pass as a parameter.
        self.isHealthy = isHealthy

    def showIfHealthy(self):
        return self.isHealthy


class Meat(Food):
    def __init__(self, name, price, isHealthy, fat, protein, isFrozen):
        #Food.__init__(self, name, price, isHealthy)
        super().__init__(name, price, isHealthy)
        # As shown above, there are two ways to inherit. By using super() function, there is no need
        #  to use the name of the parent class, in addition, "self" is not required to pass as a parameter.
        self.fat = fat
        self.protein = protein
        self.isFrozen = isFrozen

    def showIfFrozen(self):
        return self.isFrozen


px = Meat('Steak', 20.2, True, 0.0823, 0.1415, True)


print("Is the product {} frozen? ".format(px.name), px.isFrozen)
print("The price of product {} is: ".format(
    px.name), "$" + str(px.price) + "/package")
print("The fat content of product {} is: ".format(
    px.name), str(round(px.fat*100, 2)) + "%")
print("The protein content of product {} is: ".format(
    px.name), str(round(px.protein*100, 2)) + "%")
print("Is the product {} healthy? ".format(px.name), px.showIfHealthy())
