# -*- coding: utf-8 -*-

import numpy as np
from numpy import linalg as LA
import math

def regular(matrix, vector, E):
    
    #pq = vector/LA.norm(vector)
    
    currentLamb = 0
    prevLamb = 0
    
    X = matrix.dot(vector)
    
    e = E + 1
    
    while(e > E):
        
        
        prevLamb = currentLamb
        
             
        q = X/LA.norm(X)
                
        X = matrix.dot(q)
        
        currentLamb = (q.T.dot(X))/q.T.dot(q)
                
        e = abs((currentLamb - prevLamb)/currentLamb)
        
   
    q = X/LA.norm(X)
    
    return currentLamb,q

def inverse(matrix, vector, E):
    
    inv = LA.inv(matrix)
    
    lamb,X = regular(inv,vector,E)
    
    lamb = 1/lamb
    
    return lamb,X


def desloc(matrix,vector,mi,E):
    
  #I = np.array([[1,0,0],
  #              [0,1,0],
  #              [0,0,1]])  
   
  I = np.identity(6)  
  A = matrix - (mi*I)

  lamb,X = inverse(A,vector,E)

  lamb += mi

  return lamb,X  

    
        
    