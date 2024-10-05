# coding: utf-8
import numpy as np
def calc_one_loop(new_points, points):
    m = len(new_points)
    n = len(points)
    d = np.zeros((m, n))
    
    for i in range(m):
        # Calculate the distance between the new point and all the points
        d[i] = np.sum(np.square(new_points[i] - points), axis=1)
        
    return d
