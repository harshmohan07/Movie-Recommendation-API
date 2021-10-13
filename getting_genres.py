from omdb import OMDBClient

client = OMDBClient(apikey="918dc733")

def get_genres(Name):
    movie = client.get(title=Name)
    try:
        genres = movie['genre'].split(',')
    except:
        genres = []
    return genres
