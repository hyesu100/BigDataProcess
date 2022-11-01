#!/usr/bin/python3
import sys

input_file = sys.argv[1] 
output_file = sys.argv[2]

genres = dict()
with open(input_file, "rt") as fp:
    for row in fp:
            row = row.replace("\n","")
            movies = row.split("::")
            genre = movies[2].split("|")

            for g in genre:
                if g not in genres:
                    genres[g] = 1
                else:
                    genres[g] += 1

with open(output_file, "wt") as fp:
    for key, value in genres.items():
        fp.write(key + " " + str(value) + "\n")
