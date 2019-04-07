# -*- coding: utf-8 -*-

import numpy as np
import scipy.linalg as LA

    
ri = 0.2
rf = 0.5

deltaR = (rf-ri)/10

r = ri

A = np.zeros((9,9));
    
for i in range(1,10):
            
      c1 = ((14/(deltaR**2)) - 14/(r*2*deltaR))
      
      c2 = -28/(deltaR**2)
    
      c3 = ((14/(deltaR**2)) +   14/(r*2*deltaR))
      
      if i > 1:
          A[i-1][i-2] = c1
      
      A[i-1][i-1] = c2
      
      if i < 9:
          A[i-1][i] = c3
          
    
      print('Equation ' + str(i))
      print(str(c1) + 'y' + str(i-1) + ' ' + str(c2) + 'y' + str(i) + ' ' + str(c3) + 'y' + str(i+1))  
        
      r += deltaR
      
   
#A = np.array([[-13600,7480,0,0,0],
#              [6233.33,-13600,7366.66,0,0],
#              [0,6314.28,-13600,7285.71,0],
#              [0,0,6375,-13600,7225],
#              [0,0,0,6422.22,-13600]])
    
B = [-13,-13,-13,-13,-13,-13,-13,-13,-13]

y = LA.solve(A,B)

print(y)