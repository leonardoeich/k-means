import pandas as pd
import math
import random
import statistics 
#from kmeans import k_means

def manhattan_distance(p1, p2):
  total = 0
  for i in range(len(p1)):
    total += abs(p1[i] - p2[i])
  return total

def euclidean_distance(p1, p2):
  total = 0
  for i in range(len(p1)):
    total += pow((p1[i] - p2[i]), 2)
  return math.sqrt(total)

def get_max_min(axis):
  # get max and min from an axis
  min_point = axis.min()
  max_point = axis.max()
  
  return min_point, max_point

def random_centroid(data):
  # passes arround all axis getting random numbers (along with max and min)
  point = []
  for axis in range(len(data.columns)):
    min_point, max_point = get_max_min(data.iloc[:,axis])
    point.append(random.uniform(min_point, max_point))
  return point

def take_means(data):
  point = []
  # taking the mean of each axis to compute new centroid
  for axis in range(len(data[0])):
      #print(range(len(data[0])))
      #print(data[30])
      point.append(data[axis].mean())
  return point

def calculate_centroids(data, clusters, attributes_list):
  centroids = []
  for cluster in clusters:
    point = []
    cluster_data = data.iloc[cluster]
    for attribute in attributes_list:
      point.append(cluster_data[attribute].mean())
    centroids.append(point)
  return centroids

def calculate_distance_intra_cluster(data, clusters, centroids):
  aggregate_distance = 0
  #go through each centroid
  for i, centroid in enumerate(centroids):
    #get the rows of each centroid
    cluster = clusters[i]
    for row in cluster:
      #calculate the distance for the given centroid
      row_values = data.iloc[row]
      distance = pow(euclidean_distance(centroid, row_values), 2)
      aggregate_distance += distance    
  return aggregate_distance

def lists_are_equal(l1, l2):
  equal = True
  if (len(l1) != len(l2)):
    equal = False
  else:
    for i in range(len(l1)):
      if (l1[i] != l2[i]):
        equal = False
  return equal



def read_attribute_list(file_path):
  with open(file_path) as f:
    content = f.read()
    content = content.rstrip("\n")
    attributes_list = content.split(" ")
  return attributes_list

def normalize_categorical(data):
  if data == 'female':
    return 1
  if data == 'male':
    return 0
  if pd.isnull(data):
    return random.uniform(0,1)
