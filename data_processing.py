import numpy as np
from operator import add
import pandas as pd
from scipy import spatial
import math
import csv
from smart_open import open
from data_calling_func import *
from getting_genres import *
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
from gensim.models import Word2Vec
import gensim
from json import JSONEncoder
import json

class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)


def PipelineModel(name):

    lis = get_genres(name)
    if lis == []:
        return {'Error' : 'Wrong Movie Name Typed'}
    is_new = False
    model = gensim.models.keyedvectors.KeyedVectors.load_word2vec_format('/Users/hmk/Desktop/GoogleNews-vectors-negative300.bin', binary=True)#IMPORT THE ADDRESS
    movie_to_vect_dict,movie_to_genre_dict,final_dict,genre_vectors = call_data()
    for i in range(len(lis)):
        if lis[i] == "Sci-Fi":
            lis[i]  = "Futuristic"
        if lis[i] == "Film-Noir":
            lis[i] = "Fatalism"
    vec = [0]*300
    for i in lis:
        if i in genre_vectors.keys():
            vec = np.add(vec,genre_vectors[i])
        else :
            try:
                new_vec = model[i]
                genre_vectors[i] = new_vec
                vec = np.add(vec,new_vec)
            except:
                lis.remove(i)
    ans_vect = np.divide(vec,len(lis))
    if name not in movie_to_vect_dict.keys():
        print(1)
        is_new = True
        movie_to_vect_dict[name] = ans_vect
        movie_to_genre_dict[name] = lis
        max = 0
        for key in genre_vectors:
            maxcs = 0
            name1 = ""
            cosine_similarity = 1 - spatial.distance.cosine(genre_vectors[key], ans_vect)
            if cosine_similarity > maxcs:
                maxcs = cosine_similarity
                name1 = key
            final_dict[name1].append(name)
        
    predict = {}        
    movies_form_each_genre = math.ceil(15/len(lis))
    for i in lis:
        mov = {}
        for j in final_dict[i]:
            out = 1 - spatial.distance.cosine(movie_to_vect_dict[j], ans_vect)
            mov[j] = out
        sort_orders = sorted(mov.items(), key=lambda x: x[1], reverse=True)
        temp = movies_form_each_genre
        for i in sort_orders:
            predict[i[0]] = movie_to_genre_dict[i[0]]
            temp -= 1
            if temp == 0:
                break
    if is_new == True:
        with open("Movie2Vector.json", "w") as write_file:
            json.dump(movie_to_vect_dict, write_file, cls=NumpyArrayEncoder)
        with open("Genre2Vector.json", "w") as write_file:
            json.dump(genre_vectors, write_file, cls=NumpyArrayEncoder)
        with open("Genre2ItsMovies.json", "w") as write_file:
            json.dump(final_dict, write_file, cls=NumpyArrayEncoder)
        with open("Movie2ItsGenre.json", "w") as write_file:
            json.dump(movie_to_genre_dict, write_file, cls=NumpyArrayEncoder)
    return predict
    












            
            
