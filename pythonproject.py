# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import requests

url = 'https://ghibliapi.herokuapp.com/films/'
response = requests.get(url)
file = open("ghibli_studio.json", "w+", encoding='utf-8') #ho aggiunto encoding pechè non leggeva il giapponese nel json
print(file.name)
file.writelines(response.text)
file.close()

import json
import pandas


json_data = json.load(open("ghibli_studio.json", encoding= 'utf-8'))

all_movies = json_data[0:]

csv_file_path = 'merged_ghibli.csv'
df = pandas.DataFrame(all_movies)


df.columns = ['id', 'title', 'original_title', 'original_title_romanised','image','movie_banner','description','director','producer','release_date','running_time','rt_score','people','species','locations','vehicols','url']

df.to_csv(csv_file_path, index=False)


print(df['title']) #to get all the titles 

print(df['title'][2]) #to print the second movie 

print(df['people'])

print(df['description'][2])





    






