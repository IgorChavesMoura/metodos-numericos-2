# -*- coding: utf-8 -*-

import numpy as np
import scipy.linalg as LA


Le = 0.3/7

K = np.array([[14*Le/3,-7*Le/6],
              [-7*Le/6,7*Le/2]])
f = np.array([13*Le/2,13*Le/2])


A = np.zeros((6,6))

elements = np.array([[0,1],
                     [1,2],
                     [2,3],
                     [3,4],
                     [4,5],
                     [5,6]])
B = np.zeros(6)

for el in elements:
    
    for i in range(2):
        for j in range(2):
            
            I = el[i]
            J = el[j]
            
            if  I < 6 and J < 6:
                A[I][J] += K[i][j]
                
    for i in range(2):
        I = el[i]
        
        if I < 6:
            B[I] += f[i]  
        
        
            
y = LA.solve(A,B)