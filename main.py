import pandas as pd
from utils import *
from kmeans import k_means
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.decomposition import PCA


def main():
  
  data = pd.read_csv(r'./data/Personality_Vars.txt', sep = '\t')
  #data1 = pd.read_csv(r'./data/Personality_Vars.txt', sep = '\t')
  #data2 = pd.read_csv(r'./data/SocioDemographic_Vars.txt', sep = '\t')
  #data2 = data2.replace('female', int(1))
  #data2 = data2.replace('male', int(0))
  #data2['Gender'] = data2['Gender'].apply(normalize_categorical)

  with open('columns') as f:
    content = f.read()
    content = content.rstrip("\n")
    attributes_list = content.split(" ")
  
  #n_iterations = 100
  data_subset = data[attributes_list]
  
  

  '''
  with open('columns2') as f:
    content = f.read()
    content = content.rstrip("\n")
    attributes_list2 = content.split(" ")

  data_subset2 = data2[attributes_list2]

  attributes_list.extend(attributes_list2)

  data = pd.concat([data_subset,data_subset2], axis=1)
  #print(data.to_string())
  #print(attributes_list)
  #return
  '''
  
  n_iterations = 100
  intra = []
  
  k = 3
  best_centroids, best_clusters = k_means(data_subset, k, attributes_list)
  min_intra_distance = calculate_distance_intra_cluster(data_subset, best_clusters, best_centroids)
  
  #add cluster column
  data_subset['Cluster'] = ""
  for i, cluster in enumerate(best_clusters):
    for row in cluster:
      data_subset.loc[row+1, 'Cluster'] = i

  X = data_subset[attributes_list]

  pca = PCA(n_components=2)
  components = pca.fit_transform(X)

  fig = px.scatter(components, x=0, y=1, color=data_subset['Cluster'])
  fig.show()

  ###########

  #df = px.data.iris()
  #features = ["sepal_width", "sepal_length", "petal_width", "petal_length"]

  fig = px.scatter_matrix(
      data_subset,
      dimensions=attributes_list,
      color="Cluster"
  )
  fig.update_traces(diagonal_visible=False)
  fig.show()
  
  #data_subset['Cluster'] = cluster


  '''
  for i in range(n_iterations):
    centroids, clusters = k_means(data_subset, k, attributes_list)
    intra_distance = calculate_distance_intra_cluster(data_subset, clusters, centroids)
    if intra_distance < min_intra_distance:
      min_intra_distance = intra_distance
      best_centroids = centroids.copy()
      best_clusters = clusters.copy()

  
  
  

  n_iterations = 100
  distances = []
  for i in range(n_iterations):
    centroids, clusters = k_means(data_subset, 12, attributes_list)
    intra_distance = calculate_distance_intra_cluster(data_subset, clusters, centroids)
    centroids, clusters = k_means(data, 10, attributes_list)
    intra_distance = calculate_distance_intra_cluster(data, clusters, centroids)
    distances.append(intra_distance)
    #if intra_distance < min_intra_distance:
    #  min_intra_distance = intra_distance
    #  best_centroids = centroids.copy()
    #  best_clusters = clusters.copy()

  
  print(min(distances))
  #print(intra_distance)

  # x axis values
  x = [1,2,3,4,5,6]
  # corresponding y axis values
  y = [2,4,1,5,2,6]
  # plotting the points
  plt.plot(ks, intra, color='green', linestyle='solid', linewidth = 3, marker='o', markerfacecolor='blue', markersize=12)

  # setting x and y axis range
  plt.ylim(0,max(intra) + 200)
  plt.xlim(1,11)

  # naming the x axis
  plt.xlabel('number of clusters')
  # naming the y axis
  plt.ylabel('average within cluster squared error')

  # giving a title to my graph
  plt.title('Some cool customizations!')

  # function to show the plot
  plt.show()
  
  '''

main()
