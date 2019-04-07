# -*- coding: utf-8 -*-

import numpy as np
from numpy import linalg as LA
import math

np.set_printoptions(floatmode='unique')


def qr(T,H,E):


    
    Ak = T.copy()
    X = H.copy()
    
    e = E + 1
    
    while(e > E):
        print('\n\n\n\n')
        
        #Q,R = LA.qr(Ak)
        
        Q,R = decomposition(Ak)
        
        #Q = np.round(Q,3)
        #R = np.round(R,3)
        
        print('Q:\n',Q,'\n')
        print('R:\n',R,'\n')
        
        print('QT:\n', Q.T,'\n')
        
        Ak = R.dot(Q)
    
        #Ak = np.round(Ak,3)
    
        X = X.dot(Q)
        
        #X = np.round(X,3)
    
        print('Ak:\n', Ak,'\n')
        print('X:\n', X,'\n')

        prevE = e
        
        e = normWithoutDiagonal(Ak)
        print('e ->', e)
        
        if(e == prevE):
            break
        
    return Ak,X    

def decomposition(A):
    n = np.shape(A)[0]
    
    Aj = np.copy(A)
    
    Qk = np.identity(n)
    
    
    for j in range(n-1):
        
        JT  = build_JT(Aj,j)
        
        #JT = np.round(JT,3)
        
        print('JT:\n',JT)
        
        Aj = JT.dot(Aj)
        
        #Aj = np.round(Aj,3)
        
        print('Aj:\n', Aj)
        
        Qk = JT.dot(Qk)
        
        
        
    print('\n\n')    
    return Qk.T, Aj

def build_JT(Aj, j):
    
    n = np.shape(Aj)[0]
    
    tg = Aj[j+1][j]/Aj[j][j]
    
    ang = math.atan(tg)
    
    print('angle ->', ang)
    
    JT = np.identity(n)
    
    JT[j][j] = math.cos(ang)
    JT[j][j+1] = math.sin(ang)
    JT[j+1][j] = -(math.sin(ang))
    JT[j+1][j+1] = math.cos(ang)
    
    return JT 

def normWithoutDiagonal(matrix):
    
    n = np.shape(matrix)[0]
    
    norm = 0
    
    for i in range(n):
        for j in range(n):
            
            if i != j:
                norm += math.pow(matrix[i][j],2)

    norm = math.sqrt(norm)
    
    return norm