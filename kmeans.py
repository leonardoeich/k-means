from utils import * 

def k_means(data, k, attributes_list):
  centroids = []
  change = True
  # creating k lists (one for each cluster)
  clusters = [[] for _ in range(k)]
  # randomly create the first centroids based on the instances
  for i in range(k):
    centroids.append(random_centroid(data))

  while change:
    new_clusters = [[] for _ in range(k)]
    # find the nearest centroid for each instance
    for i in range(len(data)):
      distances = []
      # calculate the distance from the current centroids
      for j in range(k):
        distances.append(euclidean_distance(data.iloc[i], centroids[j]))

      #use index of data
      new_clusters[distances.index(min(distances))].append(i)

    #if all points are in the same cluster, then we are finished
    if (lists_are_equal(clusters, new_clusters)):
      change = False

    if (change):
      clusters = new_clusters.copy()
      centroids = calculate_centroids(data, clusters, attributes_list)
  return [centroids, clusters]
