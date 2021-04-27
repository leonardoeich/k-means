import pandas as pd
data = pd.read_csv (r'./data/MusicAndMovies_Vars.txt', sep = '\t')

print (data)
print(data.iloc[0][0])
