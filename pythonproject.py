# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#authors: Olimpia Sannucci, Giulia Di Martino and Hanna Carucci Viterbi

#dataframe movies
import requests

url = 'https://ghibliapi.herokuapp.com/films/'
response = requests.get(url)
file = open("ghibli_studio.json", "w+", encoding='utf-8') 
print(file.name)
file.writelines(response.text)
file.close()

import json
import pandas

json_data = json.load(open("ghibli_studio.json", encoding= 'utf-8'))

all_movies = json_data[0:]

csv_file_path = 'merged_ghibli.csv'
df = pandas.DataFrame(all_movies)

df.drop(["original_title_romanised"], axis = 1, inplace = True)
df.drop(["image"], axis = 1, inplace = True)
df.drop(["movie_banner"], axis = 1, inplace = True)
df.drop(["people"], axis = 1, inplace = True)
df.drop(["species"], axis = 1, inplace = True)
df.drop(["locations"], axis = 1, inplace = True)
df.drop(["vehicles"], axis = 1, inplace = True)

df.to_csv(csv_file_path, index=False)


#dataframe people 
url2 = 'https://ghibliapi.herokuapp.com/people'
response2 = requests.get(url2)
file2 = open("ghibli_people.json", "w+", encoding='utf-8') 
print(file2.name)
file2.writelines(response2.text)
file2.close()

json_data2 = json.load(open("ghibli_people.json", encoding= 'utf-8'))

all_people = json_data2[0:]

df2 = pandas.DataFrame(all_people)

df2.drop(["films"], axis = 1, inplace = True)
df2.drop(["species"], axis = 1, inplace = True)
df2.drop(["gander"], axis = 1, inplace = True)

csv_file_path = 'merged_people.csv'
df2.to_csv(csv_file_path, index=False)

#dataframe locations 
url3 = 'https://ghibliapi.herokuapp.com/locations'
response3 = requests.get(url3)
file3 = open("ghibli_locations.json", "w+", encoding='utf-8') 
print(file3.name)
file3.writelines(response3.text)
file3.close()

json_data3 = json.load(open("ghibli_locations.json", encoding= 'utf-8'))

all_locations = json_data3[0:]

csv_file_path3 = 'merged_locations.csv'
df3 = pandas.DataFrame(all_locations)

df3.drop(["films"], axis = 1, inplace = True)
df3.drop(["residents"], axis = 1, inplace = True)

df3.to_csv(csv_file_path, index=False)

#dataframe vehicles
url4 = 'https://ghibliapi.herokuapp.com/vehicles'
response4 = requests.get(url4)
file4 = open("ghibli_vehicles.json", "w+", encoding='utf-8') 
print(file4.name)
file4.writelines(response4.text)
file4.close()

json_data4 = json.load(open("ghibli_vehicles.json", encoding= 'utf-8'))

all_vehicles = json_data4[0:]

csv_file_path = 'merged_vehicles.csv'
df4 = pandas.DataFrame(all_vehicles)

df4.drop(["pilot"], axis = 1, inplace = True)
df4.drop(["films"], axis = 1, inplace = True)

df4.to_csv(csv_file_path, index=False


#dataframe species 
url5 = 'https://ghibliapi.herokuapp.com/species'
response5 = requests.get(url5)
file5 = open("ghibli_species.json", "w+", encoding='utf-8') 
print(file5.name)
file5.writelines(response5.text)
file5.close()

json_data5 = json.load(open("ghibli_species.json", encoding= 'utf-8'))

all_species = json_data5[0:]

csv_file_path = 'merged_species.csv'
df5 = pandas.DataFrame(all_species)

df5.drop(["people"], axis = 1, inplace = True)
df5.drop(["films"], axis = 1, inplace = True)

df5.to_csv(csv_file_path, index=False)

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec
from IPython import get_ipython 

#dataframe 1
df.drop(["id"], axis = 1, inplace = True)
df.drop(["url"], axis = 1, inplace = True)
df.drop(["original_title"], axis = 1, inplace = True)
df.drop(["description"], axis = 1, inplace = True)
from numpy import array



#number of films by each producer
df["producer"].value_counts().plot(kind='bar', title='Number of films per producer\n', color="blue")
#numer of films by each director 
df["director"].value_counts().plot(kind='bar', title='Number of films per director\n', color="green")

plt.hist(df['release_date'], color='purple', edgecolor='black') #brutto



#first step is to find the distribution of each gender in the dataframe "people"
male = df2.loc[df2['gender'] == 'Male']. count()[0]
female = df2.loc[df2['gender'] == 'Female']. count()[0]
other=len(df2) - male - female 



#remove columns
df2.drop(["id"], axis = 1, inplace = True)
df2.drop(["url"], axis = 1, inplace = True)

#pie plot gender
#function count() to transform non numerical variables 
df2.groupby('gender')['gender'].count().plot.pie(autopct='%.2f',figsize=(5,5))
#pie with eye color 
df2.groupby('eye_color')['eye_color'].count().plot.pie(autopct='%.2f',figsize=(5,5))
#pie with hair color
df2.groupby('hair_color')['hair_color'].count().plot.pie(autopct='%.2f',figsize=(5,5))



#dataframe 3 locations 
df3.drop(["id"], axis = 1, inplace = True)
df3.drop(["url"], axis = 1, inplace = True)
#pie plot terrain
df3.groupby('terrain')['terrain'].count().plot.pie(autopct='%.2f',figsize=(5,5))
#pie sul clima
df3.groupby('climate')['climate'].count().plot.pie(autopct='%.2f',figsize=(5,5))
#distribuzione del clima 
df3["climate"].value_counts().plot(kind='bar', title='climate distribution \n', color="green")
df3["terrain"].value_counts().plot(kind='bar', title='terrain distribution \n', color="green")


#dataframe 4 vechicles
#remove columns
df4.drop(["id"], axis = 1, inplace = True)
df4.drop(["url"], axis = 1, inplace = True)
#pie plot vehicles
df4.groupby('vehicle_class')['vehicle_class'].count().plot.pie(autopct='%.2f',figsize=(5,5))


#dataframe 5 species
#remove columns
df5.drop(["id"], axis = 1, inplace = True)
df5.drop(["url"], axis = 1, inplace = True)
#pie
df5.groupby('name')['name'].count().plot.pie(autopct='%.2f',figsize=(5,5))


