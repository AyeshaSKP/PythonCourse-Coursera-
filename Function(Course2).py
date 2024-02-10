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
    a = divide(int)
    return a + 2

print(sum(100))