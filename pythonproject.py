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
file2 = open("ghibli_people.json", "w+", encoding='utf-8') #ho aggiunto encoding pechè non leggeva il giapponese nel json
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
file3 = open("ghibli_locations.json", "w+", encoding='utf-8') #ho aggiunto encoding pechè non leggeva il giapponese nel json
print(file3.name)
file3.writelines(response3.text)
file3.close()

json_data3 = json.load(open("ghibli_locations.json", encoding= 'utf-8'))

all_locations = json_data3[0:]

csv_file_path3 = 'merged_locations.csv'
df3 = pandas.DataFrame(all_locations)

df3.drop(["films"], axis = 1, inplace = True)
df3.drop(["species"], axis = 1, inplace = True)
df3.drop(["gander"], axis = 1, inplace = True)
df3.drop(["residents"], axis = 1, inplace = True)

#dataframe vehicles
url4 = 'https://ghibliapi.herokuapp.com/vehicles'
response4 = requests.get(url4)
file4 = open("ghibli_vehicles.json", "w+", encoding='utf-8') #ho aggiunto encoding pechè non leggeva il giapponese nel json
print(file4.name)
file4.writelines(response4.text)
file4.close()

json_data4 = json.load(open("ghibli_vehicles.json", encoding= 'utf-8'))

all_vehicles = json_data4[0:]

csv_file_path = 'merged_vehicles.csv'
df4 = pandas.DataFrame(all_vehicles)

df4.drop(["pilot"], axis = 1, inplace = True)
df4.drop(["films"], axis = 1, inplace = True)


#dataframe species 
url5 = 'https://ghibliapi.herokuapp.com/species'
response5 = requests.get(url5)
file5 = open("ghibli_species.json", "w+", encoding='utf-8') #ho aggiunto encoding pechè non leggeva il giapponese nel json
print(file5.name)
file5.writelines(response5.text)
file5.close()

json_data5 = json.load(open("ghibli_species.json", encoding= 'utf-8'))

all_species = json_data5[0:]

csv_file_path = 'merged_species.csv'
df5 = pandas.DataFrame(all_species)

df5.drop(["people"], axis = 1, inplace = True)
df5.drop(["films"], axis = 1, inplace = True)



