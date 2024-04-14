#Class and Inheritance
#Create a class called NumberSet that accepts 2 integers as input, and defines two instance variables: num1 and num2, which hold each of the input integers. Then, create an instance of NumberSet where its num1 is 6 and its num2 is 10. Save this instance to a variable t.

class NumberSet:
    def __init__(self,x,y):
        self.num1=x
        self.num2=y
t = NumberSet(6,10)   

#Create a class called Animal that accepts two numbers as inputs and assigns them respectively to two instance variables: arms and legs. Create an instance method called limbs that, when called, returns the total number of limbs the animal has. To the variable name spider, assign an instance of Animal that has 4 arms and 4 legs. Call the limbs method on the spider instance and save the result to the variable name spidlimbs.
class Animal:
    """class"""
    def __init__(self,x,y):
        self.arms=x
        self.legs=y
    def limbs(self):
        return (self.arms+self.legs)
    
spider=Animal(4,4)
spidlimbs=spider.limbs()
print(spidlimbs)

#Create a class called Cereal that accepts three inputs: 2 strings and 1 integer, and assigns them to 3 instance variables in the constructor: name, brand, and fiber. When an instance of Cereal is printed, the user should see the following: “[name] cereal is produced by [brand] and has [fiber integer] grams of fiber in every serving!” To the variable name c1, assign an instance of Cereal whose name is "Corn Flakes", brand is "Kellogg's", and fiber is 2. To the variable name c2, assign an instance of Cereal whose name is "Honey Nut Cheerios", brand is "General Mills", and fiber is 3. Practice printing both!
class Cereal:
    def __init__(self,x,y,in1):
        self.name=x
        self.brand=y
        self.fiber=in1
    def getX(self):
        return self.name
    def getY(self):
        return self.brand
    def getZ(self):
        return self.fiber
    def __str__(self):
        return"{} cereal is produced by {} and has {} grams of fiber in every serving!".format(self.name,self.brand,self.fiber)
    
c1=Cereal("Corn Flakes","Kellogg's",2)
print(c1)
c2=Cereal("Honey Nut Cheerios","General Mills",3)
print(c2)
#in th eupper funcion there is no special function if there was you would call them
class Cereal:
    def __init__(self,x,y,in1):
        self.name=x
        self.brand=y
        self.fiber=in1
    def getX(self):
        return self.name
    def getY(self):
        return self.brand
    def getZ(self):
        return self.fiber
    def newfunction(self):
        return (str(self.name)*self.fiber)
    def __str__(self):
        return"{} cereal is produced by {} and has {} grams of fiber in every serving!".format(self.name,self.brand,self.fiber)
    
c1=Cereal("Corn Flakes","Kellogg's",2)
print(c1)
c1new=c1.newfunction
c2=Cereal("Honey Nut Cheerios","General Mills",3)
print(c2)


#Assignment
#Define a class called Bike that accepts a string and a float as input, and assigns those inputs respectively to two instance variables, color and price. Assign to the variable testOne an instance of Bike whose color is blue and whose price is 89.99. Assign to the variable testTwo an instance of Bike whose color is purple and whose price is 25.0.
class Bike:
    def __init__(self,n1,n2):
        self.color=n1
        self.price=n2
testOne=Bike("blue",89.99)
testTwo=Bike("purple",25.0)


#Create a class called AppleBasket whose constructor accepts two inputs: a string representing a color, and a number representing a quantity of apples. The constructor should initialize two instance variables: apple_color and apple_quantity. Write a class method called increase that increases the quantity by 1 each time it is invoked. You should also write a __str__ method for this class that returns a string of the format: "A basket of [quantity goes here] [color goes here] apples." e.g. "A basket of 4 red apples." or "A basket of 50 blue apples." (Writing some test code that creates instances and assigns values to variables may help you solve this problem!)

class AppleBasket():
    def __init__(self,c,q):
        self.apple_color=c
        self.apple_quantity=q

    def getX(self):
        return self.apple_color
    
    def getY(self):
        return self.apple_quantity
    
    def increase(self):
         self.apple_quantity += 1
    
    def __str__(self):
        return"A basket of {} {} apples.".format(self.apple_quantity,self.apple_color)

#Define a class called BankAccount that accepts the name you want associated with your bank account in a string, and an integer that represents the amount of money in the account. The constructor should initialize two instance variables from those inputs: name and amt. Add a string method so that when you print an instance of BankAccount, you see "Your account, [name goes here], has [start_amt goes here] dollars." Create an instance of this class with "Bob" as the name and 100 as the amount. Save this to the variable t1.
class BankAccount():
    def __init__(self,stringg,intt):
        self.name=stringg
        self.amt= intt

    def __str__(self):
        return "Your account, {}, has {} dollars.".format(self.name,self.amt)
    
    def getX(self):
        return self.name
    def getY(self):
        return self.amt
t1= BankAccount("Bob",100)
print(t1)