import pandas as pd
from utils import *
from kmeans import k_means
import matplotlib.pyplot as plt


def main():
  data1 = pd.read_csv(r'./data/Personality_Vars.txt', sep = '\t')
  data2 = pd.read_csv(r'./data/SocioDemographic_Vars.txt', sep = '\t')
  #data2 = data2.replace('female', int(1))
  #data2 = data2.replace('male', int(0))
  data2['Gender'] = data2['Gender'].apply(normalize_categorical)

  with open('columns') as f:
    content = f.read()
    content = content.rstrip("\n")
    attributes_list = content.split(" ")

  data_subset = data1[attributes_list]

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
  n_iterations = 50
  intra = []
  ks = []

  #k = 3
  #best_centroids, best_clusters = k_means(data_subset, 2, attributes_list)
  #min_intra_distance = calculate_distance_intra_cluster(data_subset, best_centroids, best_clusters)
  #intra.append(min_intra_distance)

  for k in range(2, 11):
    ks.append(k)
    distances = []
    for i in range(n_iterations):
      centroids, clusters = k_means(data_subset, k, attributes_list)
      intra_distance = calculate_distance_intra_cluster(data_subset, clusters, centroids)
      distances.append(intra_distance)
      #if intra_distance < min_intra_distance:
      #  min_intra_distance = intra_distance
      #  best_centroids = centroids.copy()
      #  best_clusters = clusters.copy()
    intra.append(min(distances))
  '''

  n_iterations = 100
  distances = []
  for i in range(n_iterations):
    centroids, clusters = k_means(data, 10, attributes_list)
    intra_distance = calculate_distance_intra_cluster(data, clusters, centroids)
    distances.append(intra_distance)
    #if intra_distance < min_intra_distance:
    #  min_intra_distance = intra_distance
    #  best_centroids = centroids.copy()
    #  best_clusters = clusters.copy()


  print(min(distances))
  '''
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
