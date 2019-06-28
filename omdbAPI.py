import requests
import json

def getMovieDetails(id):
    url = "http://www.omdbapi.com/?i="+id+"&apikey=feb37c8d"
    res = requests.get(url)
    # jsonData = json.dumps(res.content) 
    # data = json.loads(res)
    return res.json()["Title"]
movieId = input('Enter movie id (IMDB id): ')
print(movieId)
movieName = input('Enter movie name (IMDB id): ')
print(movieName)
# print(getMovieDetails())