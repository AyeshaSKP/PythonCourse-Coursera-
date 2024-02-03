#Python Couresra
# Python Basics  
# Week 1

import turtle
wn = turtle.Screen()
ayesha = turtle.Turtle()
#ayesha.forward(90)
#ayesha.right(40)
ayesha.left(90)
#ayesha.right(50)
ayesha.forward(90)
ayesha.right(90)
ayesha.salary = 900
print(ayesha.salary)
print(ayesha.right)


# Week2 
addition_str = "2+5+10+20"
# you cant convert string to int so you conver it to a list
addition_str=addition_str.split("+")
print(addition_str)
# now trun the list to int
#for i in addition_str:
    #print(int(i))

#type(i)

for i in range(0,len(addition_str)):
    addition_str[i]=int(addition_str[i])

print(addition_str)
#now sum up
accum=0
for i in addition_str:
    accum=accum+i

sum_val=accum
print(sum_val)



#another question
original_str = "The quick brown rhino jumped over the extremely lazy fox."

accum=0
for str in original_str:
    accum=accum+1
    
num_chars=accum
print(num_chars)

original_str = "The quick brown rhino jumped over the extremely lazy fox."

accum=0
for str in range(0,len(original_str)):
    accum=accum+1
    
num_chars=accum
print(num_chars)
# another question

week_temps_f = "75.1,77.7,83.2,82.5,81.0,79.5,85.7"
week_temps_f=week_temps_f.split(",")

#list to float
for i in range(0,len(week_temps_f)):
    week_temps_f[i]=float(week_temps_f[i])
print(week_temps_f)

#sum up
accum=0
for i in week_temps_f:
    accum=accum+i
print(accum)
#How many items
#for i in week_temps_f:
    #accum1=0
    #accum1=accum1+i
#print(accum1)

#How many items
accum1=len(week_temps_f)
print(accum1)
#average
avg_temp= accum/accum1
print(avg_temp)

nums=[1,2,3,4,9,7,0,6]
print(len(nums))
for w in nums:
    accum2=0
    accum2=accum2+w
print(accum2)

#Write code to create a list of word lengths for the words in original_str using the accumulation pattern and assign the answer to a variable num_words_list. (You should use the len function).
original_str = "The quick brown rhino jumped over the extremely lazy fox"
#use only when you want the length of total string
num_words_list=list(range(0,len(original_str)))
print(num_words_list)

# if you want list of EVERY WORD
original_str = "The quick brown rhino jumped over the extremely lazy fox"
#creae empty list
num_words_list=[]
# convert string to list
#it has been done to since the question asked for a list
#otherwise we could use use string to loop over
# you have to change the name here from origiginal str to anything otherwise it wont work
original_list = original_str.split()
# for loop to iteratate over the list
for word in original_list:
    #add it to list
    num_words_list.append(len(word))
   

print(num_words_list)

#Write one for loop to print out each character of the string my_str on a separate line.
my_str = "MICHIGAN"

for str in my_str:
    print(str)

#Write code to add ‘horseback riding’ to the third position (i.e., right before volleyball) in the list sports     
    
sports = ['cricket', 'football', 'volleyball', 'baseball', 'softball', 'track and field', 'curling', 'ping pong', 'hockey']
sports.insert(2, 'horseback riding')

#Write code to take ‘London’ out of the list trav_dest.
trav_dest = ['Beirut', 'Milan', 'Pittsburgh', 'Buenos Aires', 'Nairobi', 'Kathmandu', 'Osaka', 'London', 'Melbourne']

print(trav_dest.index("London"))
trav_dest.pop(7)
print(trav_dest)

# if any lenth of any word is less than 2 and print the word

original_str = "The quick brown rhino jumped over the extremely lazy fox"
original_list=original_str.split()
print(original_list)
num_words_list=[]

for s in original_list:
    if len(s) > 2:
        num_words_list.append(len(s))
        print(s)
    
print(num_words_list)

#Create an empty string and assign it to the variable lett. Then using range, write code such that when your code is run, lett has 7 b’s ("bbbbbbb").
lett=''
for i in range(7):
    lett=lett+'b'
    
print(lett)

#Write a program that uses the turtle module and a for loop to draw something. It doesn’t have to be complicated, but draw something different than we have done in the past. (Hint: if you are drawing something complicated, it could get tedious to watch it draw over and over. Try setting .speed(10) for the turtle to draw fast, or .speed(0) for it to draw super fast with no animation.)
import turtle

python=turtle.Turtle()
see=turtle.Screen()
python.speed(10)
python.shape('turtle')
a=10
b=20
c=60
for i in range(3):
    python.left(a)
    python.right(b)
    python.forward(c)


# Week3
# Conditional Statements
#Create one conditional to find whether “false” is in string str1. If so, assign variable output the string “False. You aren’t you?”. Check to see if “true” is in string str1 and if it is then assign “True! You are you!” to the variable output. If neither are in str1, assign “Neither true nor false!” to output.
str1 ="Today you are you! That is truer than true! There is no one alive who is you-er than you!"

#if "false" in str1:
       #output= “False. You aren’t you?”
#elif "true" in str1:
       #output=“True! You are you!”
#else:
       #output=“Neither true nor false!” 


#Create an empty list called resps. Using the list percent_rain, for each percent, if it is above 90, add the string ‘Bring an umbrella.’ to resps, otherwise if it is above 80, add the string ‘Good for the flowers?’ to resps, otherwise if it is above 50, add the string ‘Watch out for clouds!’ to resps, otherwise, add the string ‘Nice day!’ to resps. Note: if you’re sure you’ve got the problem right but it doesn’t pass, then check that you’ve matched up the strings exactly.
percent_rain = [94.3, 45, 100, 78, 16, 5.3, 79, 86]

resps = []

for i in percent_rain:
    if i > 90:
        resps.append('Bring an umbrealla')
    elif i > 80:
        resps.append('Good for the flowers?')
    elif i > 50:
        resps.append('Watch out for clouds!')
    else:
         resps.append('Nice day!')
        
percent_rain = [94.3, 45, 100, 78, 16, 5.3, 79, 86]

resps = []

#Create an empty list called resps. Using the list percent_rain, for each percent, if it is above 90, add the string ‘Bring an umbrella.’ to resps, otherwise if it is above 80, add the string ‘Good for the flowers?’ to resps, otherwise if it is above 50, add the string ‘Watch out for clouds!’ to resps, otherwise, add the string ‘Nice day!’ to resps. Note: if you’re sure you’ve got the problem right but it doesn’t pass, then check that you’ve matched up the strings exactly
for i in percent_rain:
    if i > 90:
        resps.append("Bring an umbrella.")
    elif i >80:
        resps.append("Good for the flowers?")                   
    elif i > 50:
        resps.append("Watch out for clouds!")
    else:
        resps.append("Nice day!")
        
#For each string in the list words, find the number of characters in the string. If the number of characters in the string is greater than 3, add 1 to the variable num_words so that num_words should end up with the total number of words with more than 3 characters.
words = ["water", "chair", "pen", "basket", "hi", "car"]
num_words=0
for s in words:
    print(len(s))
    if len(s)>3:
        num_words = num_words+1

print(num_words)

#For each word in words, add ‘d’ to the end of the word if the word ends in “e” to make it past tense. Otherwise, add ‘ed’ to make it past tense. Save these past tense words to a list called past_tense.
words = ["adopt", "bake", "beam", "confide", "grill", "plant", "time", "wave", "wish"]
past_tense=[]

for s in words:
    if (s[-1]) == "e":
        past_tense.append(s +"d")
    else:
        past_tense.append(s + "ed")

#rainfall_mi is a string that contains the average number of inches of rainfall in Michigan for every month (in inches) with every month separated by a comma. Write code to compute the number of months that have more than 3 inches of rainfall. Store the result in the variable num_rainy_months. In other words, count the number of items with values > 3.0.
rainfall_mi = "1.65, 1.46, 2.05, 3.03, 3.35, 3.46, 2.83, 3.23, 3.5, 2.52, 2.8, 1.85"   

rainfall_milist= rainfall_mi.split(',')
num_rainy_months =[]

for s in range(0,len(rainfall_milist)):
    rainfall_milist[s]=float(rainfall_milist[s])

for s in rainfall_milist:
    if s >3.0:
        num_rainy_months.append(s)

print((num_rainy_months))
print(len(num_rainy_months))

# correct way

list= rainfall_mi.split(',')
num_rainy_months=0
for s in list:
    if float(s)>3.0:
        num_rainy_months=num_rainy_months+1
print(num_rainy_months)


# The variable sentence stores a string. Write code to determine how many words in sentence start and end with the same letter, including one-letter words. Store the result in the variable same_letter_count
sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"
list = sentence.split(' ')
print(list)
print(list[0])

same_letter_count =0
for s in list:
    if s[0]==s[-1] :
        same_letter_count = same_letter_count +1
        
print(same_letter_count)

#Write code to count the number of strings in list items that have the character w in it. Assign that number to the variable acc_num.
items = ["whirring", "wow!", "calendar", "wry", "glass", "", "llama","tumultuous","owing"]

acc_num=0

for s in items:
    if 'w' in s:
        acc_num = acc_num + 1
        
print(acc_num)

#Write code that counts the number of words in sentence that contain either an “a” or an “e”. Store the result in the variable num_a_or_e.
sentence = "python is a high level general purpose programming language that can be applied to many different classes of problems."
list = sentence.split()
num_a_or_e = 0

for s in list:
    if "a" in s or "e" in s:
        num_a_or_e = num_a_or_e + 1
        
print(num_a_or_e)


#Write code that will count the number of vowels in the sentence s and assign the result to the variable num_vowels. For this problem, vowels are only a, e, i, o, and u. Hint: use the in operator with vowels.
s = "singing in the rain and playing in the rain are two entirely different situations but both can be fun"
vowels = ['a','e','i','o','u']

# Write your code here.
#s_list = s.split()
num_vowels=0

for element in s:
    if element in vowels :
        num_vowels = num_vowels + 1
        
print(num_vowels)

# Week 4 on Mutattable and Non mutattable way in list and string and String format
#Write code to add ‘horseback riding’ to the third position (i.e., right before volleyball) in the list sports
sports = ['cricket', 'football', 'volleyball', 'baseball', 'softball', 'track and field', 'curling', 'ping pong', 'hockey']
sports.insert(2,'horseback riding')
print(sports)

# week 4
# Accumulating through lists
#For each word in the list verbs, add an -ing ending. Save this new list in a new list, ing.
verbs = ["kayak", "cry", "walk", "eat", "drink", "fly"]

ing=[]

for s in verbs:
    ing.append(s + "ing")

print(ing)

#Given the list of numbers, numbs, create a new list of those same numbers increased by 5. Save this new list to the variable newlist.
numbs = [5, 10, 15, 20, 25]
newlist=[]
for i in numbs:
    newlist.append(i+ 5)

print(newlist)
# Non mutating
# Another way of doing it
for i in numbs:
    newlist =newlist +[i+5]

print(newlist)

#Given the list of numbers, numbs, modifiy the list numbs so that each of the original numbers are increased by 5. Note this is not an accumulator pattern problem, but its a good review
numbs = [5, 10, 15, 20, 25]

    
print(numbs)
numbs[0:5]=[10,15,20,25,30]
print(numbs)
#Assign an empty string to the variable output. Using the range function, write code to make it so that the variable output has 35 a s inside it (like "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"). Hint: use the accumulation pattern!
output="" #here do not give space inside the string if you give it will show extra space in th result

for i in range(35):
    a= i
    output = output + "a"
    
print(output)
print(len(output))