#Nested Data Structures

#Nested List
# Below, we have provided a list of lists. Use indexing to assign the element ‘horse’ to the variable name idx1.
animals = [['cat', 'dog', 'mouse'], ['horse', 'cow', 'goat'], ['cheetah', 'giraffe', 'rhino']]

idx1= animals[1][0]

#Using indexing, retrieve the string ‘willow’ from the list and assign that to the variable plant.
data = ['bagel', 'cream cheese', 'breakfast', 'grits', 'eggs', 'bacon', [34, 9, 73, []], [['willow', 'birch', 'elm'], 'apple', 'peach', 'cherry']]
data = ['bagel', 'cream cheese', 'breakfast', 'grits', 'eggs', 'bacon', [34, 9, 73, []], [['willow', 'birch', 'elm'], 'apple', 'peach', 'cherry']]
plant= data[7][0][0]
#Nested Dictionary

#JSON

#Nested Iteration
#Below, we have provided a list of lists that contain information about people. Write code to create a new list that contains every person’s last name, and save that list as last_names.
info = [['Tina', 'Turner', 1939, 'singer'], ['Matt', 'Damon', 1970, 'actor'], ['Kristen', 'Wiig', 1973, 'comedian'], ['Michael', 'Phelps', 1985, 'swimmer'], ['Barack', 'Obama', 1961, 'president']]

last_names=[]
for l in info:
    for e in l:
        last_names.append(l[1])

print(last_names)
#upper code will print the names four times
# this code will print the name one time
info = [['Tina', 'Turner', 1939, 'singer'], ['Matt', 'Damon', 1970, 'actor'], ['Kristen', 'Wiig', 1973, 'comedian'], ['Michael', 'Phelps', 1985, 'swimmer'], ['Barack', 'Obama', 1961, 'president']]

last_names=[]
for l in info:
    
        last_names.append(l[1])

print(last_names)

#Below, we have provided a list of lists named L. Use nested iteration to save every string containing “b” into a new list named b_strings.
L = [['apples', 'bananas', 'oranges', 'blueberries', 'lemons'], ['carrots', 'peas', 'cucumbers', 'green beans'], ['root beer', 'smoothies', 'cranberry juice']]
b_strings=[]
for l in L:
     for e in l:
          if "b" in e:
               b_strings.append(e)

print(b_strings)
# Data Structures

# Shallow and Deep Copies

#he variable nested contains a nested list. Assign ‘snake’ to the variable output using indexing.
nested = [['dog', 'cat', 'horse'], ['frog', 'turtle', 'snake', 'gecko'], ['hamster', 'gerbil', 'rat', 'ferret']]
output= nested[1][2]
print(output)

#Below, a list of lists is provided. Use in and not in tests to create variables with Boolean values. See comments for further instructions.

lst = [['apple', 'orange', 'banana'], [5, 6, 7, 8, 9.9, 10], ['green', 'yellow', 'purple', 'red']]
for l in lst:
    if type(l) is list:
        for e in l:
            if type(e) is list:
                if "yellow" in e:
                    print(True)
                else:
                     print(False)


for l in lst:
    if "yellow" in lst[2]:
         yellow= True
print(yellow)

for four in lst:
    if 4 in lst[1]:
         four=True
    else:
        four=False

print(four)

for l in lst:
    if "orange" in lst[0]:
          orange= True
    else:
          orange=False
    
print(orange)
     
#      Below, we’ve provided a list of lists. Use in statements to create variables with Boolean values - see the ActiveCode window for further directions.
L = [[5, 8, 7], ['hello', 'hi', 'hola'], [6.6, 1.54, 3.99], ['small', 'large']]

# Test if 'hola' is in the list L. Save to variable name test1
for l in L:
    if "hola" in L:
        test1 = True
    else:
        test1= False
print(test1)
# Test if [5, 8, 7] is in the list L. Save to variable name test2
for l in L:
    if [5,8,7] in L:
        test2= True
    else:
        test2= False
print(test2)
# Test if 6.6 is in the third element of list L. Save to variable name test3
for l in L:
    if 6.6 in L[2]:
        test3= True
    else:
        test3= False
print(test3)


#Provided is a nested data structure. Follow the instructions in the comments below. Do not hard code.
nested = {'data': ['finding', 23, ['exercises', 'hangout', 34]], 'window': ['part', 'whole', [], 'sum', ['math', 'calculus', 'algebra', 'geometry', 'statistics',['physics', 'chemistry', 'biology']]]}

# Check to see if the string 'data' is a key in nested, if it is, assign True to the variable data, otherwise assign False.
for key in nested.keys():
    if 'data' in nested:
        data=True
    else:
        data= False
print(data)
# Check to see if the integer 24 is in the value of the key data, if it is then assign to the variable twentyfour the value of True, otherwise False.
for k,v in nested.items():
    if nested['data']==24:
        twentyfour=True
    else:
        twentyfour = False
        
print(twentyfour)
        
# Check to see that the string 'whole' is not in the value of the key window. If it's not, then assign to the variable whole the value of True, otherwise False.
for k,v in nested.items():
    if nested['window']== 'whole':
        whole= True
    else:
        whole= False
print(whole)
# Check to see if the string 'physics' is a key in the dictionary nested. If it is, assign to the variable physics, the value of True, otherwise False.
for k in nested.keys():
    if 'physics' in nested:
        physics=True
    else:
        physics= False
print(physics)


#Iterate through the contents of l_of_l and assign the third element of sublist to a new list called third.

l_of_l = [['purple', 'mauve', 'blue'], ['red', 'maroon', 'blood orange', 'crimson'], ['sea green', 'cornflower', 'lavender', 'indigo'], ['yellow', 'amarillo', 'mac n cheese', 'golden rod']]

third=[]
for l in l_of_l:
    #for e in l:
        third.append(l[2])

#Given below is a list of lists of athletes. Create a list, t, that saves only the athlete’s name if it contains the letter “t”. If it does not contain the letter “t”, save the athlete name into list other.
 
athletes = [['Phelps', 'Lochte', 'Schooling', 'Ledecky', 'Franklin'], ['Felix', 'Bolt', 'Gardner', 'Eaton'], ['Biles', 'Douglas', 'Hamm', 'Raisman', 'Mikulak', 'Dalton']]

t=[]
other=[]

for l in athletes:
    for e in l:
        if "t" in e:
            t.append(e)
        else:
            other.append(e)       

#The variable nested_d contains a nested dictionary with the gold medal counts for the top four countries in the past three Olympics. Assign the value of Great Britain’s gold medal count from the London Olympics to the variable london_gold. Use indexing. Do not hardcode.
 
nested_d = {'Beijing':{'China':51, 'USA':36, 'Russia':22, 'Great Britain':19}, 'London':{'USA':46, 'China':38, 'Great Britain':29, 'Russia':22}, 'Rio':{'USA':35, 'Great Britain':22, 'China':20, 'Germany':13}}
london_gold = nested_d['London']['Great Britain']

# Below, we have provided a nested dictionary. Index into the dictionary to create variables that we have listed in the ActiveCode window.

sports = {'swimming': ['butterfly', 'breaststroke', 'backstroke', 'freestyle'], 'diving': ['springboard', 'platform', 'synchronized'], 'track': ['sprint', 'distance', 'jumps', 'throws'], 'gymnastics': {'women':['vault', 'floor', 'uneven bars', 'balance beam'], 'men': ['vault', 'parallel bars', 'floor', 'rings']}}

# Assign the string 'backstroke' to the name v1
v1=sports['swimming'][2]
# Assign the string 'platform' to the name v2
v2= sports['diving'][1]
# Assign the list ['vault', 'floor', 'uneven bars', 'balance beam'] to the name v3
v3=['vault', 'floor', 'uneven bars', 'balance beam']

# Assign the string 'rings' to the name v4
v4='rings'

#Given the dictionary, nested_d, save the medal count for the USA from all three Olympics in the dictionary to the list US_count.



nested_d = {'Beijing':{'China':51, 'USA':36, 'Russia':22, 'Great Britain':19}, 'London':{'USA':46, 'China':38, 'Great Britain':29, 'Russia':22}, 'Rio':{'USA':35, 'Great Britain':22, 'China':20, 'Germany':13}}

US_count=[]


for k,v in nested_d.items():
    #for k1,v1 in nested_d.items():
        if 'USA' in v:
            US_count.append(v["USA"])
print(US_count)
    

          