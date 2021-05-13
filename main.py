import pandas as pd
from utils import *
from kmeans import *
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.decomposition import PCA


def main():
  
  #data = pd.read_csv(r'./data/Personality_Vars.txt', sep = '\t')
  data1 = pd.read_csv(r'./data/Personality_Vars.txt', sep = '\t')
  data2 = pd.read_csv(r'./data/SocioDemographic_Vars.txt', sep = '\t')
  data2 = data2.replace('female', int(1))
  data2 = data2.replace('male', int(0))
  
  attributes_list = read_attribute_list('columns')
  attributes_list2 = read_attribute_list('columns2')
  
  data_subset = data1[attributes_list]
  data_subset2 = data2[attributes_list2]

  #attributes_list.extend(attributes_list2)

  #data = pd.concat([data_subset,data_subset2], axis=1)
  #data = data.dropna()
  data_subset = data_subset.reset_index(drop=True)

  best_centroids, best_clusters = generate_best_clusters(data_subset, 3, 10, attributes_list)

  data_subset['Cluster'] = ""
  for i, cluster in enumerate(best_clusters):
    for row in cluster:
      data_subset.loc[row, 'Cluster'] = i
      
  X = data_subset[attributes_list]

  pca = PCA(n_components=2)
  components = pca.fit_transform(X)

  fig = px.scatter(data_subset, x=attributes_list[0], y=attributes_list[1], color=data_subset['Cluster'])
  fig.show()
  
main()
