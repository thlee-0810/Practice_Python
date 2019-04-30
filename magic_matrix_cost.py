# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 00:23:49 2019

@author: EdLee
"""
'''
Reference: 
    Minimum cost to convert 3 X 3 matrix into magic square (GeeksforGeeks)
'''
import numpy as np

mat = [ [ 4, 9, 2 ],
       [ 3, 5, 7 ],
       [ 8, 1, 5 ]];    # 1
mat2 = [[ 4, 8, 2 ],
        [4, 5, 7 ],
        [6, 1, 6 ]];    # 4

def build_magic_3():
    '''
    Build up all the combination of 3*3 magic matrix.
    '''
    mag_matrix = np.array([[8,1,6],[3,5,7],[4,9,2]])
    mm=[]
    mm.append(mag_matrix)
    mm.append(mag_matrix.T)
    mm.append(np.flipud(mag_matrix))
    mm.append(np.flipud(mag_matrix).T)
    mm.append(np.fliplr(mag_matrix))
    mm.append(np.fliplr(mag_matrix).T)
    mm.append(np.fliplr(np.flipud(mag_matrix)))
    mm.append(np.fliplr(np.flipud(mag_matrix)).T)
    return mm
def find_min_cost(target):
    '''
    Compute the minimum cost to convert a matrix to magic matrix.
    cost compute: from 3->1: |3-1| = 2
    :type target: list - 3*3 matrix
    :rtype: int - cost of transform
    '''
    mm = build_magic_3()
    min_cost = 5
    for i in mm:
        cost = np.sum(abs(target-i),axis=None)
        if cost<min_cost:
            min_cost = cost
    return min_cost

print(find_min_cost(mat2))