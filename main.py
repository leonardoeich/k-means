import pandas as pd
from utils import *
from kmeans import k_means

def main():
  
  data = pd.read_csv(r'./data/MusicAndMovies_Vars.txt', sep = '\t')
  
  with open('columns') as f:
    content = f.read()
    content = content.rstrip("\n")
    attributes_list = content.split(" ")
  
  k = len(data)
  data_subset = data[attributes_list]
  centroids, clusters = k_means(data_subset, k, attributes_list)
  intra_distance = calculate_distance_intra_cluster(data_subset, clusters, centroids)

  print(intra_distance)

  #print(data.iloc[0][0])
  #print(centroids)
  #print(len(clusters[0]) + len(clusters[1]) + len(clusters[2]) + len(clusters[3]))
  #print(len(data))

main()