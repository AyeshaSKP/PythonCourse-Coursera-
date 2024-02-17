# List_Comprehension
#The for loop below produces a list of numbers greater than 10. Below the given code, use list comprehension to accomplish the same thing. Assign it the the variable lst2. Only one line of code is needed.
L = [12, 34, 21, 4, 6, 9, 42]
lst2=[value for value in L if value>10]
lst3=[lambda value:value for value in L if value]
print(lst2)
print(lst3)

#rite code to assign to the variable compri all the values of the key name in any of the sub-dictionaries in the dictionary tester. Do this using a list comprehension.
tester = {'info': [{"name": "Lauren", 'class standing': 'Junior', 'major': "Information Science"},{'name': 'Ayo', 'class standing': "Bachelor's", 'major': 'Information Science'}, {'name': 'Kathryn', 'class standing': 'Senior', 'major': 'Sociology'}, {'name': 'Nick', 'class standing': 'Junior', 'major': 'Computer Science'}, {'name': 'Gladys', 'class standing': 'Sophomore', 'major': 'History'}, {'name': 'Adam', 'major': 'Violin Performance', 'class standing': 'Senior'}]}
inner_list= tester['info']
import json
print(json.dumps(inner_list,indent=2))
compri= [dictionary['name']for dictionary in inner_list]
print(compri)


#Write a function called longlengths that return the the lenghths of those string that have at least 4 characters. Try that with list comprehension.
def longlenghts(list_string):
    fourc=[len(string) for string in list_string if len(string)>4]
    return fourc

print(longlenghts(["ok","hhohgihuighukhgih","euhuhwe"]))

#with map and filter 


def long(string):
    filte= filter(lambda s:len(s)>=4,string)
    new_filte=list(filte)
    n= map(len,new_filte)
    return list(n)
    
print(long(["ok","hhohgihuighukhgih","euhuhwe"]))

#zip function
#Below we have provided two lists of numbers, L1 and L2. Using zip and list comprehension, create a new list, L3, that sums the two numbers if the number from L1 is greater than 10 and the number from L2 is less than 5. This can be accomplished in one line of code.

L1 = [1, 5, 2, 16, 32, 3, 54, 8, 100]
L2 = [1, 3, 10, 2, 42, 2, 3, 4, 3]

L3= [x1+x2 for x1,x2 in list(zip(L1,L2)) if x1>10 and x2<5]
print(L3)

#Write code to assign to the variable map_testing all the elements in lst_check while adding the string “Fruit: ” to the beginning of each element using mapping.

lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']
import json
print(json.dumps(lst_check,indent=2))
map_testing= list(map(lambda x:"Fruit: "  +str(x),lst_check))
print(map_testing)

#Below, we have provided a list of strings called countries. Use filter to produce a list called b_countries that only contains the strings from countries that begin with B.

countries = ['Canada', 'Mexico', 'Brazil', 'Chile', 'Denmark', 'Botswana', 'Spain', 'Britain', 'Portugal', 'Russia', 'Thailand', 'Bangladesh', 'Nigeria', 'Argentina', 'Belarus', 'Laos', 'Australia', 'Panama', 'Egypt', 'Morocco', 'Switzerland', 'Belgium']

b_countries=  list(filter(lambda x:"B" in x[0],countries))

#Below, we have provided a list of tuples that contain the names of Game of Thrones characters. Using list comprehension, create a list of strings called first_names that contains only the first names of everyone in the original list.
people = [('Snow', 'Jon'), ('Lannister', 'Cersei'), ('Stark', 'Arya'), ('Stark', 'Robb'), ('Lannister', 'Jamie'), ('Targaryen', 'Daenerys'), ('Stark', 'Sansa'), ('Tyrell', 'Margaery'), ('Stark', 'Eddard'), ('Lannister', 'Tyrion'), ('Baratheon', 'Joffrey'), ('Bolton', 'Ramsey'), ('Baelish', 'Peter')]
first_names= [x[1] for x in people]

#Use list comprehension to create a list called lst2 that doubles each element in the list, lst.
lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]

lst_2= [x*2 for x in lst]
print(lst_2)

#Below, we have provided a list of tuples that contain students’ names and their final grades in PYTHON 101. Using list comprehension, create a new list passed that contains the names of students who passed the class (had a final grade of 70 or greater).
students = [('Tommy', 95), ('Linda', 63), ('Carl', 70), ('Bob', 100), ('Raymond', 50), ('Sue', 75)]

passed= [x[0] for x in students if x[1]>=70]
print(passed)

#Write code using zip and filter so that these lists (l1 and l2) are combined into one big list and assigned to the variable opposites if they are both longer than 3 characters each.
l1 = ['left', 'up', 'front']
l2 = ['right', 'down', 'back']
opposites= list(filter(lambda x:len(x[0])>3 and len(x[1])>3,list(zip(l1,l2))))
print(opposites)

#Below, we have provided a species list and a population list. Use zip to combine these lists into one list of tuples called pop_info. From this list, create a new list called endangered that contains the names of species whose populations are below 2500.
species = ['golden retriever', 'white tailed deer', 'black rhino', 'brown squirrel', 'field mouse', 'orangutan', 'sumatran elephant', 'rainbow trout', 'black bear', 'blue whale', 'water moccasin', 'giant panda', 'green turtle', 'blue jay', 'japanese beetle']

population = [10000, 90000, 1000, 2000000, 500000, 500, 1200, 8000, 12000, 2300, 7500, 100, 1800, 9500, 125000]

pop_info=list((x1,x2) for (x1,x2) in list(zip(species,population)))
print(pop_info)

endangeredd= list(filter(lambda x:x[1]<2500,pop_info))
print(endangeredd)

endangered= [x[0] for x in endangeredd]
print(endangered)