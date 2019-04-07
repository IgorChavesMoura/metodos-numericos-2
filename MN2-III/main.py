# -*- coding: utf-8 -*-

import numpy as np
from numpy import linalg as LA

from potentiation import potentiation 
from householder import householder,qr

A = 3 
B = 7 
C = 4 
D = 1 
E = 8 
F = 4

matrix = np.array([[50,4,3,2,1,-4],
                   [4,33,3,-3,-2,1],
                   [3,4,15,7,-3,-2],
                   [2,-3,7,52,5,0],
                   [1,-2,-3,5,25,-7],
                   [-4,1,-2,0,-7,35]])


#matrixInv = LA.inv(matrix)

#A = np.array([[4,-1,1],
#              [-1,3,-2],
#              [1,-2,3]])

#matrix2 = np.array([[3,1,4],
#                    [1,7,2],
 #                   [4,2,0]]) 

X0 = np.array([1,1,1,1,1,1])

#matrix2 = np.array([[30, 5, 2], [5, 29, 4], [2, 4, 56]])


eigenval, eigenvector= potentiation.desloc(matrix,X0,40,0.000001)

#print(eigenvector)

#eigenval, eigenvector= potentiation.inverse(matrix,X0,0.001)



Aj,H = householder.householder(matrix)


print(Aj)
print(H)

#Aj2,H2 = householder.householder(matrix2)
#Ak2, X2 = qr.qr(Aj2,H2, 0.01)
#
#AjInv, HInv = householder.householder(matrixInv)

#Aj = np.round(Aj,3)
#H = np.round(H,3)
#
#AjInv = np.round(AjInv,3)
#HInv = np.round(HInv,3)

Ak,X = qr.qr(Aj,H,0.000001)

print(Ak)
print(X)

#AkInv, XInv = qr.qr(AjInv,HInv,0.01)

#FI = H.dot(X)

#D10 = LA.matrix_power(Ak,10)

#M10 = X.dot(D10).dot(LA.inv(X))

