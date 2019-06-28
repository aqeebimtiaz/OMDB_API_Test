import requests
import json

def getMovieDetails(query):
    if(query.isdigit() == False):
        query = "t="+query
    else:
        query = "i="+query
    url = "http://www.omdbapi.com/?"+query+"&apikey=feb37c8d"
    res = requests.get(url)
    # jsonData = json.dumps(res.content) 
    # data = json.loads(res)
    return res.json()["Title"]
movieId = input("Enter movie id (IMDB id): ")
print(movieId)
movieName = input("Enter movie id (IMDB name): ")
print(movieName)
if(movieName != None):
    searchQuery = movieName
else:
    searchQuery = movieId
print(getMovieDetails(searchQuery))