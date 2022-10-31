#!/usr/bin/python3
import sys

input_file = sys.argv[1] 
output_file = sys.argv[2]

genres = dict()
with open(input_file, "rt") as fp:
    data = fp.readlines()

    for row in fp:
        movie = row.split("::")
        genre = movie[2].split("|")

        for g in genre:
            if g not in genres:
                genres[g] = 1
            else:
                genres[g] += 1

with open(output_file, "wt") as fp:
    for key in genres.keys():
        fp.write(key + " " + str(genres[key]) + "\n")
