# importing the module
import pandas as pd
import csv
import numpy
from googlesearch import search
# taking input from user
val = input("Enter your command: ")
#splitting the command to subparts
K = val.split()
T = len(K)

def queryreform():
  search_name = 'Brooks'
  with open('tmdb_5000_movies.csv', 'r') as file: 
    output = re.findall(f'{search_name}.*', file.read())
  for row in output:
    items = row.split(',')
    print(items[0], '>>' ,items[1])

def similar():




def searchit():
  from googlesearch import search

  for i in search(query, tld="co.in", num=1, stop=10, pause=2):
    print(i)

#splitting the cases based on command length

if T == 0:
  print("Error: no commands!")
elif T == 1:
  query = "allintext:"
  query = query.append(#columns)
  searchit()
  print(x)
elif T == 2:
  query = "allintext:"
  query = query.append(#columns)
  searchit()
elif T == 3:
  query = "allintext:"
  query = query.append(#columns
  searchit()
else:
  print("Error: Too many commands!")
