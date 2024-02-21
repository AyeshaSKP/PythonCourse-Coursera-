#Reuest
#python -m ensurepip --default-pip
#raspython3 -m pip install requests
import requests
import json

d= {"about":"careers"}
results=requests.get("http://www.google.com/search",params=d)
print(results.url)
print(results.text)

#converting it to apython dictionary or list
print(results.json)

# convert to string
#x1= json.dumps(x,indent=2)
#print(x1)

#example
#STEP 01
#importing module
import requests

# STEP 02
 #setting up response object and key val
 
# page = requests.get("https://api.datamuse.com/words?rel_rhy=funny")
kval_pairs = {'rel_rhy': 'funny'}
page = requests.get("https://api.datamuse.com/words", params=kval_pairs)

# STEP 03
 # printing as text and url
 
print(page.text[:150]) # print the first 150 characters
print(page.url) # print the url that was fetched

 # STEP 04
 #turning to list or dictionary from response object and printing the type
x= page.json()
print(type(x))

#STEP 05
#Making human readable and that is why ising  dumps for string
print(json.dumps(x,indent=2))


