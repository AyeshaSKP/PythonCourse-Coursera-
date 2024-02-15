#Function
#Write a function named same that takes a string as input, and simply returns that string.
def same (string):
    return string
print(same("hello"))

#Write a function called same_thing that returns the parameter, unchanged.
def same_thing (paramater):
    return paramater

print(same_thing("ijjpjo"))

#Write a function called subtract_three that takes an integer or any number as input, and returns that number minus three.
def subtract_three(integer):
    return integer-3

print(subtract_three(9))

# Write a function called change that takes one number as its input and returns that number, plus 7.
def change (number):
    return number+7
print(change(7))

#. Write a function named intro that takes a string as input. This string ist intended to be a person’s name and the output is a standardized greeting. For example, given the string “Becky” as input, the function should return: “Hello, my name is Becky and I love SI 106.”
def intro(name):
    return ("Hello, my name is {} and I love SI 106".format(name))

print(intro("Becky"))
print(intro(12))

def intro(str1):
    return("Hello, my name is "+ str1+ " and I love SI 106.")

intro("Becky") #calling the function named intro
               #and passing the parameter Becky

#. Write a function called decision that takes a string as input, and then checks the number of characters. If it has over 17 characters, return “This is a long string”, if it is shorter or has 17 characters, return “This is a short string”.
def decision (string):
    for c in string:
        if len(string)>17:
            return ("This is a long string")
        else:
            return ("This is a short string")

print(decision("jgugiuhiuhjjjjjjjohiucciigihouh"))
print(decision("hh"))

# Write a function called count that takes a list of numbers as input and returns a count of the number of elements in the list.
def count(list):
    accum = 0
    for element in list:
        accum = accum+ 1
    return accum

y = [2,4,6,9,0,5,6,9]
print(count(y))

#Write a function called int_return that takes an integer as input and returns the same integer.
def int_return(int):
    return int

int_return(12)

#Write a function called add that takes any number as its input and returns that sum with 2 added.
def add(int):
    return int +2
print(add(2))

#Write a function called change that takes any string, adds “Nice to meet you!” to the end of the argument given, and returns that new string.
def change(string):
    return("{}Nice to meet you!".format(string))
print(change("Ayehsa"))

#Write a function, accum, that takes a list of integers as input and returns the sum of those integers.

def accum(list):
    accum = 0
    for element in list:
        accum = accum +element
    return accum
y= [1,2,3]
print(accum(y))

#Write a function, length, that takes in a list as the input. If the length of the list is greater than or equal to 5, return “Longer than 5”. If the length is less than 5, return “Less than 5”.
def length(list):
    if len(list) >= 5:
        return("Longer than 5")
    else:
        return("Less than 5")
    
    return len(list)

y= [1,2,4,7,9,0,4,6,8]
newY = length(y)
print(newY)


#You will need to write two functions for this problem. The first function, divide that takes in any number and returns that same number divided by 2. The second function called sum should take any number, divide it by 2, and add 6. It should return this new number. You should call the divide function within the sum function. Do not worry about decimals.
# here int are different for two different functions
def divide(int):
    return (int//2)

def sum(int):
    a = divide(int) # calling a function
    return a + 2

print(sum(100))

#Write a function called str_mult that takes in a required string parameter and an optional integer parameter. The default value for the integer parameter should be 3. The function should return the string multiplied by the integer parameter.

def str_mult(x,y=3):
    return (str(x) *y)

string="la"
print(str_mult(string))

# Define a function called multiply. It should have one required parameter, a string. It should also have one optional parameter, an integer, named mult_int, with a default value of 10. The function should return the string multiplied by the integer. (i.e.: Given inputs “Hello”, mult_int=3, the function should return “HelloHelloHello”)

def multiply(string,mult_int=10):
    return(str(string)*mult_int)

print(multiply("how are you"))

#Currently the function is supposed to take 1 required parameter, and 2 optional parameters, however the code doesn’t work. Fix the code so that it passes the test. This should only require changing one line of code.


def waste(mar,var = "Water",marble = "type"):
    final_string = var + " " + marble + " " + mar
    return final_string

#Create a function called mult that has two parameters, the first is required and should be an integer, the second is an optional parameter that can either be a number or a string but whose default is 6. The function should return the first parameter multiplied by the second.
def mult(integar,anything=6):
    return ((int(integar))*anything)

print(mult(555))

#The following function, greeting, does not work. Please fix the code so that it runs without error. This only requires one change in the definition of the function.
#previusly
#def greeting(greeting="Hello ", name, excl="!"):
    #return greeting + name + excl

#print(greeting("Bob"))
#print(greeting(""))
#print(greeting("Bob", excl="!!!"))

#corrected
def greeting(name, greeting="Hello ", excl="!"):
    return greeting + name + excl

print(greeting("Bob"))
print(greeting(""))
print(greeting("Bob", excl="!!!"))

#Below is a function, sum, that does not work. Change the function definition so the code works. The function should still have a required parameter, intx, and an optional parameter, intz with a defualt value of 5.
#previosuly
#def sum(intz=5, intx):
    #return intz + intx
#corrected
def sum(intx,intz=5):
    return intz + intx

#Write a function, test, that takes in three parameters: a required integer, an optional boolean whose default value is True, and an optional dictionary, called dict1, whose default value is {2:3, 4:5, 6:8}. If the boolean parameter is True, the function should test to see if the integer is a key in the dictionary. The value of that key should then be returned. If the boolean parameter is False, return the boolean value “False
def test(integer,boolean="True",dict1={2:3,4:5,6:8}):
    if boolean == "True":
        if integer in dict1.keys():
            return dict1[integer]
    elif boolean == "False":
         return False  
    
    return boolean

#Write a function called checkingIfIn that takes three parameters. The first is a required parameter, which should be a string. The second is an optional parameter called direction with a default value of True. The third is an optional parameter called d that has a default value of {'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}. Write the function checkingIfIn so that when the second parameter is True, it checks to see if the first parameter is a key in the third parameter; if it is, return True, otherwise return False.
def checkingIfIn(string,direction="True",d ={'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}):
    if direction == "True":
        if str(string) in d.keys():
            return True
        else:
            return False
    else:
        
        if str(string) not in d.keys():
            return True
        else:
            return False
    
    return direction

print(checkingIfIn("ffu"))
print(checkingIfIn("apple"))
print(checkingIfIn("apple","False"))
print(checkingIfIn("carrot"))

#We have provided the function checkingIfIn such that if the first input parameter is in the third, dictionary, input parameter, then the function returns that value, and otherwise, it returns False. Follow the instructions in the active code window for specific variable assignmemts.
def checkingIfIn(a, direction = True, d = {'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}):
    if direction == True:
        if a in d:
            return d[a]
        else:
            return False
    else:
        if a not in d:
            return True
        else:
            return d[a]
    

c_false =(checkingIfIn("lala"))
c_true =(checkingIfIn("lala","False"))
fruit_ans= checkingIfIn("fruit")
param_check =(checkingIfIn(a="new",d={'new':8}))
# do not use print since in tthe question it only says to call the function