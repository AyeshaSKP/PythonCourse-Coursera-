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
