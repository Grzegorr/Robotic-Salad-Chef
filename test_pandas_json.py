import pandas as pd
import json



# Music dataset
track_name = ['Señorita', 'China', 'Beautiful People (feat. Khalid)', 'Ransom','Goodbyes (Feat. Young Thug)']
artist_name = ['Shawn Mendes', 'Anuel AA', 'Ed Sheeran', 'Lil Tecca', 'Post Malone' ]
genre = ['canadian pop', 'reggaeton flow', 'pop', 'trap music', 'dfw rap']
beats = [117, 105, 93, 180, 150]
energy = [55, 81, 65, 64, 65]
popularity = [79, 92, 86, 92, 94]

# creating a dataframe
df = pd.DataFrame({'Track name': track_name, 'Artist name': artist_name, 'Genre': genre, 'Beats': beats, 'Energy': energy, 'Popularity': popularity})
#print(df)

#string_json = df.to_json(path_or_buf='json_test.json', orient='split', index=True)
string_json = df.to_json(orient='split', index=True)
print(string_json)

array_of_dfs = [string_json, string_json]
print(array_of_dfs)
with open('json_test.json', 'w') as f:
    json.dump(array_of_dfs, f)

#read_df = pd.read_json('json_test.json', orient='split')
#print(read_df)

with open('json_test.json', 'r') as f:
  array_read = json.load(f)
print(array_read)

for i in range(len(array_read)):
    print("Entry no " + str(i))
    read_df = pd.read_json(array_read[i], orient='split')
    print(read_df)
