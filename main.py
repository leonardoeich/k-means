import pandas as pd
import kmeans as Kmeans
import utils as ut

data = pd.read_csv(r'./data/MusicAndMovies_Vars.txt', sep = '\t')
subset = data.iloc[0:100,:]
#Kmeans.k_means(subset, 3)
Kmeans.k_means(data, 3)

#print(data)
#print(data.iloc[0][0])
#print(len(data.columns))
