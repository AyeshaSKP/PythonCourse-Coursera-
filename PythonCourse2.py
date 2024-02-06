#Python coursera
# Course 2

# Files, Dictionary, Functions, Tuple, While Loop, Advanced functions and Sorting

# Week1 
# Reading, Opening, Writting and Closing files
#Write code to find out how many lines are in the file emotion_words.txt as shown above. Save this value to the variable num_lines. Do not use the len method.
file = open("emotion_words.txt", "r")
contents = file.readlines()

num_lines = 0
for line in contents:
    num_lines = num_lines +1
    
print(num_lines)

# do not worry about the file since it is not here 

#Using the file school_prompt2.txt, find the number of characters in the file and assign that value to the variable num_char.
file = open("school_prompt2.txt","r")
contents = file. readlines()

num_char =0
for line in contents:
    for char in line:
        num_char = num_char +1
        

print(num_char)

#Create a string called first_forty that is comprised of the first 40 characters of emotion_words2.txt.

file = open("emotion_words2.txt", "r")

first_forty = ""
contents = file.readlines()
nchar = 0
for line in contents:
    for char in line:
        nchar = nchar + 1
print(nchar)


for char in line:
    if len(nchar) == 40:
        first_forty = first_forty + char
            
print(first_forty)

# another way
file = open("emotion_words2.txt", "r")

first_forty = ""
contents = file.readlines()


for line in contents[0]:
    for char in line:
        first_forty = first_forty + char[0:41]
            
        
        
            
print(first_forty)
print(len(first_forty))       

# correct way
file = open("emotion_words2.txt", "r")
first_forty = file.read(40)
print(first_forty)

 #   The textfile, travel_plans.txt, contains the summer travel plans for someone with some commentary. Find the total number of characters in the file and save to the variable num.
  file = open("travel_plans.txt", "r")
num = 0

for line in file:
    for char in line:
        num = num + 1
print(num)

#We have provided a file called emotion_words.txt that contains lines of words that describe emotions. Find the total number of words in the file and assign this value to the variable num_words.
file = open("emotion_words.txt", "r")
contents = file.readlines()
num_words = 0

for line in contents:
    num_words = num_words + len(line.split())
    
print(num_words)

#Assign to the variable num_lines the number of lines in the file school_prompt.txt.
file = open("school_prompt.txt", "r")

num_lines = 0

for line in file:
    num_lines = num_lines +1
    
print(num_lines)

#Using the file school_prompt.txt, assign the third word of every line to a list called three.

file = open ("school_prompt.txt","r")
three = []

for line in file:
    three.append(line.split()[2])
    
print(three)

# Using the file school_prompt.txt, if the character ‘p’ is in a word, then add the word to a list called p_words.
file = open("school_prompt.txt","r")
p_words=[]
for line in file:
    word= line.split()
    for w in word:
        if 'p' in w:
            p_words.append(w)
print(p_words)
