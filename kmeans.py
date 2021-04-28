import utils as ut

def k_means(data, k):
    centroid = []
    # creating k lists (one for each cluster)
    clusters = [[] for _ in range(k)]

    # randomly create the first centroids based on the instances
    for i in range(k):
        centroid.append(ut.random_centroid(data))

    # find the closest centroid for each instance
    for i in range(len(data)):
        distances = []
        # calculate the distance from the current centroids
        # (TODO change to be generic)
        for j in range(k):
            distances.append(ut.euclidean_distance(data.iloc[i], centroid[j]))
        
        # assotiating the instance to the closest centroid 
        clusters[distances.index(min(distances))].append(data.iloc[i])

    # updating the means
    #for i in 
