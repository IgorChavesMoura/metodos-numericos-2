# -*- coding: utf-8 -*-

import numpy as np
from numpy import linalg as LA

def householder(matrix):
    
    n = np.shape(matrix)[0]
    
    H = np.identity(n)
    
    Aj = np.copy(matrix)
    
    for j in range(n-2):
    
        print('j ->', j)
        
        Hj = buildHH(Aj,j)
        
        Aj = Hj.T.dot(Aj).dot(Hj)
        
        #print(Aj)
        
        H = H.dot(Hj)
        
    return Aj,H
    
def buildHH(Aj,j):
    print(Aj)
    
    size = np.shape(Aj)[0]
    
    Hj = np.identity(size)
    
    P = np.array([0.,0.,0.,0.,0.,0.])
    
    for i in range(j+1,size):
        
        print('i ->',i)
        
        P[i] = Aj[i][j]
        
        
    NP = LA.norm(P)
    
    print('NP ->', NP)
    
    PPrime = np.array([0.,0.,0.,0.,0.,0.])
    
    sign = 1
    
    if P[j+1] > 0:
        sign = -1
    
    PPrime[j+1] = NP*sign
    
    print('P ->',P)
    print('PPrime ->', PPrime)
    
    
    N = P - PPrime
    
    
    
    n = N/LA.norm(N)
    
    print('n ->', n)
    
    nT = n.reshape(-1,1)
    
    print('nT ->', nT)
    
    nnT = np.outer(nT,n)
    
    print('nnT ->', nnT)
    
    Hj = Hj - (nnT)*2
    
    return Hj