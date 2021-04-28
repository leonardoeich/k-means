import pandas as pd
import kmeans as Kmeans
import utils as ut

data = pd.read_csv (r'./data/MusicAndMovies_Vars.txt', sep = '\t')

Kmeans.k_means(data, 3) 

#print(data)
#print(data.iloc[0][0])
#print(len(data.columns))
#print(data.iloc[:,0])
