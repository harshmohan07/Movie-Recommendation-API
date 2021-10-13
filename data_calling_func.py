import numpy as np
from json import JSONEncoder
import json

class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)

def call_data():
    with open("Movie2Vector.json", "r") as read_file:
        movie_to_vect_dict = json.load(read_file)
    with open("Movie2ItsGenre.json", "r") as read_file:
        movie_to_genre_dict = json.load(read_file)
    with open("Genre2ItsMovies.json", "r") as read_file:
        final_dict = json.load(read_file)
    with open("Genre2Vector.json", "r") as read_file:
        genre_vectors = json.load(read_file)
    return movie_to_vect_dict,movie_to_genre_dict,final_dict,genre_vectors
