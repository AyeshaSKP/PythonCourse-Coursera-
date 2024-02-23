#This project will take you through the process of mashing up data from two different APIs to make movie recommendations. The TasteDive API lets you provide a movie (or bands, TV shows, etc.) as a query input, and returns a set of related items. The OMDB API lets you provide a movie title as a query input and get back data about the movie, including scores from various review sites (Rotten Tomatoes, IMDB, etc.).
#You will put those two together. You will use TasteDive to get related movies for a whole list of titles. You’ll combine the resulting lists of related movies, and sort them according to their Rotten Tomatoes scores (which will require making API calls to the OMDB API.)
#To avoid problems with rate limits and site accessibility, we have provided a cache file with results for all the queries you need to make to both OMDB and TasteDive. Just use requests_with_caching.get() rather than requests.get(). If you’re having trouble, you may not be formatting your queries properly, or you may not be asking for data that exists in our cache. We will try to provide as much information as we can to help guide you to form queries for which data exists in the cache.
#Your first task will be to fetch data from TasteDive. The documentation for the API is at https://tastedive.com/read/api.

#Define a function, called get_movies_from_tastedive. It should take one input parameter, a string that is the name of a movie or music artist. The function should return the 5 TasteDive results that are associated with that string; be sure to only get movies, not other kinds of media. It will be a python dictionary with just one key, ‘Similar’.

T#ry invoking your function with the input “Black Panther”.

#HINT: Be sure to include only q, type, and limit as parameters in order to extract data from the cache. If any other parameters are included, then the function will not be able to recognize the data that you’re attempting to pull from the cache. Remember, you will not need an api key in order to complete the project, because all data will be found in the cache.


# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_movies_from_tastedive("Bridesmaids")
# get_movies_from_tastedive("Black Panther")
import requests_with_caching
import requests
import json

import json
import requests_with_caching


def get_movies_from_tastedive(movie):
    baseurl="https://tastedive.com/api/similar"
    param_dic={}
    param_dic["q"]=movie
    #param_dic["q"]="name"
    param_dic["type"]="movies"
    param_dic["limit"]=5
    #permanent_cache_file="movies_Cache.txt"
    response=requests_with_caching.get("https://tastedive.com/api/similar",params=param_dic)
    print(response.url)
    #py_dic = json.loads(response.text)
    #return py_dic
    return response.json()

#Please copy the completed function from above into this active code window. Next, you will need to write a function that extracts just the list of movie titles from a dictionary returned by get_movies_from_tastedive. Call it extract_movie_titles.
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
#extract_movie_titles(get_movies_from_tastedive("Tony Bennett"))
# extract_movie_titles(get_movies_from_tastedive("Black Panther"))

import json
import requests_with_caching


def get_movies_from_tastedive(movie):
    baseurl="https://tastedive.com/api/similar"
    param_dic={}
    param_dic["q"]=movie
    #param_dic["q"]="name"
    param_dic["type"]="movies"
    param_dic["limit"]=5
    #permanent_cache_file="movies_Cache.txt"
    response=requests_with_caching.get("https://tastedive.com/api/similar",params=param_dic)
    print(response.url)
    #py_dic = json.loads(response.text)
    #return py_dic
    return response.json()

def extract_movie_titles(movie):
    #q=get_movies_from_tastedive(movie)
    moviess=[]
    
    for n in movie['Similar']['Results']:
        moviess.append(n['Name'])
     
    return moviess
    
#q=get_movies_from_tastedive("Black Panther")
print(extract_movie_titles(get_movies_from_tastedive("Black Panther")))
            



#Please copy the completed functions from the two code windows above into this active code window. Next, you’ll write a function, called get_related_titles. It takes a list of movie titles as input. It gets five related movies for each from TasteDive, extracts the titles for all of them, and combines them all into a single list. Don’t include the same movie twice.

# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_related_titles(["Black Panther", "Captain Marvel"])
# get_related_titles([])


import json
import requests_with_caching


def get_movies_from_tastedive(movie):
    baseurl="https://tastedive.com/api/similar"
    param_dic={}
    param_dic["q"]=movie
    #param_dic["q"]="name"
    param_dic["type"]="movies"
    param_dic["limit"]=5
    #permanent_cache_file="movies_Cache.txt"
    response=requests_with_caching.get("https://tastedive.com/api/similar",params=param_dic)
    print(response.url)
    #py_dic = json.loads(response.text)
    #return py_dic
    return response.json()

def extract_movie_titles(movie):
    #q=get_movies_from_tastedive(movie)
    moviess=[]
    
    for n in movie['Similar']['Results']:
        moviess.append(n['Name'])
     
    return moviess
def get_related_titles(list_movie):
    related_movies=[]
    
    for l in list_movie:
        function1=get_movies_from_tastedive(l)
        function2 = extract_movie_titles(function1)
        for e in function2:
            related_movies.append(e)
    return list(set(related_movies))#set will ensure that the items are uncommon and since it returns set object we need to use list


print(get_related_titles(["Black Panther", "Captain Marvel"]))

#Your next task will be to fetch data from OMDB. The documentation for the API is at https://www.omdbapi.com/

#Define a function called get_movie_data. It takes in one parameter which is a string that should represent the title of a movie you want to search. The function should return a dictionary with information about that movie.

#Again, use requests_with_caching.get(). For the queries on movies that are already in the cache, you won’t need an api key. You will need to provide the following keys: t and r. As with the TasteDive cache, be sure to only include those two parameters in order to extract existing data from the cache.
import json
import requests_with_caching


def get_movie_data(movie):
    baseurl="http://www.omdbapi.com/"
    param_dic={}
    param_dic["t"]=movie
    #param_dic["q"]="name"
    #param_dic["type"]="movies"
    #param_dic["limit"]=5
    param_dic["r"]='json'
    #permanent_cache_file="movies_Cache.txt"
    response=requests_with_caching.get(baseurl,params=param_dic)
    print(response.url)
    #py_dic = json.loads(response.text)
    #return py_dic
    return response.json()

print(get_movie_data("Venom"))
print(get_movie_data("Deadpool 2"))
print(get_movie_data("Baby Mama"))

#Please copy the completed function from above into this active code window. Now write a function called get_movie_rating. It takes an OMDB dictionary result for one movie and extracts the Rotten Tomatoes rating as an integer. For example, if given the OMDB dictionary for “Black Panther”, it would return 97. If there is no Rotten Tomatoes rating, return 0.

# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
#get_movie_rating(get_movie_data("Deadpool 2"))

# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_movie_data("Venom")
# get_movie_data("Baby Mama")

import json
import requests_with_caching


def get_movie_data(movie):
    baseurl="http://www.omdbapi.com/"
    param_dic={}
    param_dic["t"]=movie
    #param_dic["q"]="name"
    #param_dic["type"]="movies"
    #param_dic["limit"]=5
    param_dic["r"]='json'
    #permanent_cache_file="movies_Cache.txt"
    response=requests_with_caching.get(baseurl,params=param_dic)
    print(response.url)
    #py_dic = json.loads(response.text)
    #return py_dic
    return response.json()

def get_movie_rating(m):
    for l in m["Ratings"]:
        if l["Source"]=="Rotten Tomatoes":
            v= l["Value"].replace("%","")
            print(type(v))
            v1=int(v)
            print(type(v1))
            return v1
    else:
            return 0
    
 
print(get_movie_rating(get_movie_data("Deadpool 2")))
print(get_movie_rating(get_movie_data("Black Panther")))

    

#Now, you’ll put it all together. Don’t forget to copy all of the functions that you have previously defined into this code window. Define a function get_sorted_recommendations. It takes a list of movie titles as an input. It returns a sorted list of related movie titles as output, up to five related movies for each input movie title. The movies should be sorted in descending order by their Rotten Tomatoes rating, as returned by the get_movie_rating function. Break ties in reverse alphabetic order, so that ‘Yahşi Batı’ comes before ‘Eyyvah Eyvah’.

# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
 #get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"])
import json
import requests_with_caching

import json
import requests_with_caching


def get_movies_from_tastedive(movie):
    baseurl="https://tastedive.com/api/similar"
    param_dic={}
    param_dic["q"]=movie
    #param_dic["q"]="name"
    param_dic["type"]="movies"
    param_dic["limit"]=5
    #permanent_cache_file="movies_Cache.txt"
    response=requests_with_caching.get("https://tastedive.com/api/similar",params=param_dic)
    print(response.url)
    #py_dic = json.loads(response.text)
    #return py_dic
    return response.json()

def extract_movie_titles(movie):
    #q=get_movies_from_tastedive(movie)
    moviess=[]
    
    for n in movie['Similar']['Results']:
        moviess.append(n['Name'])
     
    return moviess
def get_related_titles(list_movie):
    related_movies=[]
    
    for l in list_movie:
        function1=get_movies_from_tastedive(l)
        function2 = extract_movie_titles(function1)
        for e in function2:
            related_movies.append(e)
    return list(set(related_movies))


print(get_related_titles(["Black Panther", "Captain Marvel"]))

def get_movie_data(movie):
    baseurl="http://www.omdbapi.com/"
    param_dic={}
    param_dic["t"]=movie
    #param_dic["q"]="name"
    #param_dic["type"]="movies"
    #param_dic["limit"]=5
    param_dic["r"]='json'
    #permanent_cache_file="movies_Cache.txt"
    response=requests_with_caching.get(baseurl,params=param_dic)
    print(response.url)
    #py_dic = json.loads(response.text)
    #return py_dic
    return response.json()

def get_movie_rating(m):
    for l in m["Ratings"]:
        if l["Source"]=="Rotten Tomatoes":
            v= l["Value"].replace("%","")
            print(type(v))
            v1=int(v)
            print(type(v1))
            return v1
    else:
            return 0
    
 
print(get_movie_rating(get_movie_data("Deadpool 2")))
print(get_movie_rating(get_movie_data("Black Panther")))

    

def get_sorted_recommendations(st):
    #sorted(list_of_movies,key=
    a= get_related_titles(st)
    
    i=(sorted(a,key=lambda x:(get_movie_rating(get_movie_data(x)),x),reverse=True))
    return i
print(get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"]))