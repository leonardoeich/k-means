import math
import random
import statistics 

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
