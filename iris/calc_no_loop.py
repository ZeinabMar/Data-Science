# coding: utf-8
import numpy as np
def calc_no_loop(new_points, points):
    return np.sum([np.square(points[np.newaxis,:,i] - new_points[:,np.newaxis,i]) for i in range(4)],axis=0)
