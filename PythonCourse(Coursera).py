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