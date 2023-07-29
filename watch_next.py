# building a system that tells you what to watch next based on the word similarity of the description of movies

import spacy

nlp = spacy.load("en_core_web_md")

# read in file with movie descriptions
with open('movies.txt', 'r') as file:
    movies = file.readlines()

# plant hulk movie description
plant_hulk = '''Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, 
the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. 
Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator.'''

# define function
def watch_next(last_movie):
    similarities = []

    token = nlp(last_movie)

    for movie in movies:
        token2 = nlp(movie)
        similarity = token.similarity(token2)
        similarities.append(similarity)

# find the highest similarity in list and return movie title
    highest_similarity = max(similarities)
    index = similarities.index(highest_similarity)
    next_movie = movies[index]
    next_movie_title = next_movie.split(":")[0]
    return next_movie_title

print(watch_next(plant_hulk))