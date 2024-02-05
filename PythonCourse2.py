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
