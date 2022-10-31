#!/usr/bin/python3
import sys

input_file = sys.argv[1] 
output_file = sys.argv[2]


genres = dict()
with open(input_file, "rt") as fp:
    for row in fp:
        movies = row.split("::")
        movies_genre = list(movies[2].strip())
        genre = list(movies_genre[2].split("|"))

        for g in genre:
            if g not in genres:
                genres[g] = 1
            else:
                genres[g] += 1

with open(output_file, "wt") as fp:
    for key, value in genres.items():
        fp.write(key + " " + str(value) + "\n")
