import utils as ut

def k_means(data, k):
    centroid = []

    for i in range(k):
        # for now I'll just randomly create the first centroids based on the instances
        centroid.append(ut.random_centroid(data))




