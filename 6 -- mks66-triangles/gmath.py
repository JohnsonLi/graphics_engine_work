import math
from display import *

#vector functions
#normalize vetor, should modify the parameter
def normalize(vector):
    for i in range(len(vector)):
        vector[i] = vector[i] / (sum([j * j for j in vector]) ** (1/2.0))

#Return the dot product of a . b
def dot_product(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]

#Calculate the surface normal for the triangle whose first
#point is located at index i in polygons
def calculate_normal(polygons, i):
    p0 = polygons[i]
    p1 = polygons[i + 1]
    p2 = polygons[i + 2]
    vec = [p2[0] - p0[0], p2[1] - p0[1], p2[2] - p0[2]]
    vec1 = [p1[0] - p0[0], p1[1] - p0[1], p1[2] - p0[2]]
    return [vec[1] * vec1[2] - vec[2] * vec1[1], vec[2] * vec1[0] - vec[0] * vec1[2], vec[0] * vec1[1] - vec[1] * vec1[0]]