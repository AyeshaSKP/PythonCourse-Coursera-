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

#How to work with permanent cache
# STEP 01
import requests_with_caching
import json

#step 02
# URL, paramteres and permanent cache
parameters={"term":"Ann Arbor", "entity":"podcast"}
iTunes_response = requests_with_caching.get("https://itunes.apple.com/search", params = parameters,permanent_cache_file="itunes_cache.txt")

#STEP 02
#what if you want to make a function 
def data(string):
    baseurl="https://itunes.apple.com/search"
    param_dic={}
    param_dic{"term"}={"Ann Arbor"}
    param_dic{"entity"}={"podcast"}
    iTunes_response = requests_with_caching.get("https://itunes.apple.com/search", params = param_dic,permanent_cache_file="itunes_cache.txt")
    print(iTunes_response.url)
    return iTunes_response.json()
podcast1= data("lala")
#Step 03
# JOSN for the turn into python list or dictionary from response object
py_data = json.loads(iTunes_response.text)

#STEP 04
#CHECK list or dictionary and then do undersatnd,extract,repeat
for r in py_data["results"]:#here results is thekey of the py_data dictionary and the values are list which we are itertating
    print(r["trackname"])# the vlaue of list has a key name trackname which has values and we want that