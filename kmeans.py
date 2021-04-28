import utils as ut

def k_means(data, k, change = 1):
    centroids = []
    # creating k lists (one for each cluster)
    clusters = [[] for _ in range(k)]

    # randomly create the first centroids based on the instances
    for i in range(k):
        centroids.append(ut.random_centroid(data))

    while change:
        # find the closest centroid for each instance
        for i in range(len(data)):
            distances = []
            # calculate the distance from the current centroids
            # (TODO change to be generic)
            for j in range(k):
                distances.append(ut.euclidean_distance(data.iloc[i], centroids[j]))
        
            # assotiating the instance to the closest centroid 
            clusters[distances.index(min(distances))].append(data.iloc[i])

        # updating the centroids
        new_centroids = []
        for i in range(k):
            new_centroids.append(ut.take_means(clusters[i]))

        # checking if the centroids changed
        old = set(map(tuple, centroids))
        new = set(map(tuple, new_centroids))
        # I'll change this, I just need to see if it's working
        if old != new:
            print("different")
        else:
            print("equal")
            change = 0
