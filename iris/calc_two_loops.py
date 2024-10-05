# coding: utf-8
import numpy as np
def calc_two_loops(new_points, points):
  m = len(new_points)
  n = len(points)
  d = np.zeros((m,n))
  for i in range(m):
    for j in range(n):
      d[i,j] = np.sum([np.square(points[j,0] - new_points[i,0]),
              np.square(points[j,1] - new_points[i,1]),
              np.square(points[j,2] - new_points[i,2]),
              np.square(points[j,3] - new_points[i,3])])
  return d
