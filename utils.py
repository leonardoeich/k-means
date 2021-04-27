import math

def manhattan_distance(p1, p2):
  total = 0
  for i in range(len(p1)):
    total += abs(p1[i] - p2[i])
  return total

def euclidean_distance(p1, p2):
  total = 0
  for i in range(len(p1)):
    total += pow(p1[i] - p2[i])
  return math.sqrt(total)
