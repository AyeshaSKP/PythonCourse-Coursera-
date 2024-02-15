# While Loop, Sorting and Sorting and Breaking Ties in Dictionary (Course2)
#Write a function, sublist, that takes in a list of numbers as the parameter. In the function, use a while loop to return a sublist of the input list. The sublist should contain the same values of the original list up until it reaches the number 5 (it should not contain the number 5).
#def sublist(list):
def sublist(list):
    index =0
    sublist=[]

    while index <len(list):
        if list[index] !=5 :
            sublist.append(list[index])
        else:
            return sublist
        index = index + 1
    return sublist

#ANOTHER WAY
def sublist(list):
    index =0
    sublist=[]

    while index <len(list):
        if list[index] !=5 :
            sublist.append(list[index])
            index = index + 1
        else:
            return sublist
            
#Anotehr way - do not do this
def sublist(list):
    index =0
    sublist=[]

    while index < len(list):
        sublist.append(list[index])
        if list[index] == 5 :
            break
        index = index +1
    return sublist
list2=[6,8,1,6,5,7,8]
print(sublist(list2))
#Write a function called check_nums that takes a list as its parameter, and contains a while loop that only stops once the element of the list is the number 7. What is returned is a list of all of the numbers up until it reaches 7.
def check_nums(list):
    index =0
    sub=[]

    while index < len(list):
       
        if list[index] !=7:
            sub.append(list[index])
        else:
            return sub
        
        index = index + 1
    return sub

list1= [1,2,3,5,6,7,8,9,1,9]
print(check_nums(list1))



#Write a function, sublist, that takes in a list of strings as the parameter. In the function, use a while loop to return a sublist of the input list. The sublist should contain the same values of the original list up until it reaches the string “STOP” (it should not contain the string “STOP”).

def sublist (liststrings):
    
    list_of_strings= [] 
    index=0
    while index < len(liststrings):
        if "STOP" not in liststrings[index]:
            list_of_strings.append(liststrings[index])
            index= index + 1
        else:
            return list_of_strings
    
    return list_of_strings

string1 =["europe","hhh","STOP","FBFI"]
print(sublist(string1))

#Write a function called stop_at_z that iterates through a list of strings. Using a while loop, append each string to a new list until the string that appears is “z”. The function should return the new list.
def stop_at_z(list):
    index =0
    newlist=[]

    while index < len(list):
        if list[index] != "z":
            newlist.append(list[index])
            index = index +1 
        else:
            return newlist
    return newlist
list=["ff","ff","fugefg","gg","zzzz","z","fkuni"]
print(stop_at_z(list))

#Below is a for loop that works. Underneath the for loop, rewrite the problem so that it does the same thing, but using a while loop instead of a for loop. Assign the accumulated total in the while loop code to the variable sum2. Once complete, sum2 should equal sum1.
sum2=0
index = 0
lst = [65, 78, 21, 33]

while index < len(lst):
    sum2= sum2 + lst[index]
    index= index+1


#Write a function called beginning that takes a list as input and contains a while loop that only stops once the element of the list is the string ‘bye’. What is returned is a list that contains up to the first 10 strings, regardless of where the loop stops. (i.e., if it stops on the 32nd element, the first 10 are returned. If “bye” is the 5th element, the first 4 are returned.) If you want to make this even more of a challenge, do this without slicing
def beginning(list):
    index= 0
    newlist=[]
    while index < len(list):
        
        if list[index] != "bye"and index<10:
            newlist.append(list[index])
            index = index +1 
         
        else:
            return newlist
    
    return newlist
list=["gg","gg","gg","hhh","ayesha","bye"]
print (beginning(list))

#Sort the following dictionary based on the keys so that they are sorted a to z. Assign the resulting value to the variable sorted_keys.
dictionary = {"Flowers": 10, 'Trees': 20, 'Chairs': 6, "Firepit": 1, 'Grill': 2, 'Lights': 14}

sorted_keys= sorted(dictionary)

#. Below, we have provided the dictionary groceries, whose keys are grocery items, and values are the number of each item that you need to buy at the store. Sort the dictionary’s keys into alphabetical order, and save them as a list called grocery_keys_sorted.

groceries = {'apples': 5, 'pasta': 3, 'carrots': 12, 'orange juice': 2, 'bananas': 8, 'popcorn': 1, 'salsa': 3, 'cereal': 4, 'coffee': 5, 'granola bars': 15, 'onions': 7, 'rice': 1, 'peanut butter': 2, 'spinach': 9}

#grocery_keys_sorted= list(sorted(groceries))

#Sort the following dictionary’s keys based on the value from highest to lowest. Assign the resulting value to the variable sorted_values.
dictionary = {"Flowers": 10, 'Trees': 20, 'Chairs': 6, "Firepit": 1, 'Grill': 2, 'Lights': 14}

sorted_values= sorted(dictionary,key=lambda k:dictionary[k], reverse= True)

#Sort the following string alphabetically, from z to a, and assign it to the variable sorted_letters.
letters = "alwnfiwaksuezlaeiajsdl"
sorted_letters= (sorted(letters,reverse=True))

#Sort the list below, animals, into alphabetical order, a-z. Save the new list as animals_sorted.
animals = ['elephant', 'cat', 'moose', 'antelope', 'elk', 'rabbit', 'zebra', 'yak', 'salamander', 'deer', 'otter', 'minx', 'giraffe', 'goat', 'cow', 'tiger', 'bear']
animals_sorted= sorted(animals)

#The dictionary, medals, shows the medal count for six countries during the Rio Olympics. Sort the country names so they appear alphabetically. Save this list to the variable alphabetical.
medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}
alphabetical = sorted(medals)


#Given the same dictionary, medals, now sort by the medal count. Save the three countries with the highest medal count to the list, top_three.
medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}
top_three=[]
new= sorted(medals,key= lambda k :medals[k],reverse=True)

top_three=(new[0:3])
    
print(top_three)

#We have provided the dictionary groceries. You should return a list of its keys, but they should be sorted by their values, from highest to lowest. Save the new list as most_needed.
groceries = {'apples': 5, 'pasta': 3, 'carrots': 12, 'orange juice': 2, 'bananas': 8, 'popcorn': 1, 'salsa': 3, 'cereal': 4, 'coffee': 5, 'granola bars': 15, 'onions': 7, 'rice': 1, 'peanut butter': 2, 'spinach': 9}

most_needed=sorted(groceries,key=lambda k:groceries[k],reverse=True)

#Create a function called last_four that takes in a single ID number and returns the last four digits. For example, the number 17573005 should return 3005. Then, use the resulting function to sort the list of ids stored in the variable, ids, from lowest to highest. Save this sorted list in the variable, sorted_ids. Hint: Remember that only strings can be indexed, so conversions may be needed.
def last_four(x):
    return (str(x)[-4:-1])

ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]
sorted_ids = sorted(ids,key= last_four)
print(sorted_ids)

#
#Sort the list ids by the last four digits of each id. Do this using lambda and not using a defined function. Save this sorted list in the variable sorted_id.
ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]

sorted_id=sorted(ids,key=lambda id:str(id)[-4:-1])
print(sorted_id)

#Sort the following list by each element’s second letter a to z. Do so by using lambda. Assign the resulting value to the variable lambda_sort.
ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']

lambda_sort=sorted(ex_lst,key= lambda element : element[1])