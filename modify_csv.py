import csv
#importing pandas library
import pandas as pd
import numpy


file = open('files.csv', 'w' , encoding = 'utf-8')

global csv_file
global to_include_list

csv_file = csv.writer(file)

df = pd.read_csv('tmdb_5000_movies.csv')

#print(df.columns)

to_include_list = ["Sl.No","original_title", "release_date","popularity", "genres" , "vote_average", "vote_count"]

    # ["genres", "homepage", "keywords", "original_language", "original_title", "overview",
    #                    "popularity", "release_date",
    #                    "revenue", "runtime", "tagline", "title", "vote_average", "vote_count"]

csv_file.writerow(to_include_list)

global value
value=1

def add (row) :

    global csv_file
    global value
    final_row=[value]
    value += 1

    for i in to_include_list[1:]:
        final_row.append(row[i])

    #print(final_row)

    csv_file.writerow(final_row)



df.apply(add,axis=1)
# print("Executed Succesfully")
