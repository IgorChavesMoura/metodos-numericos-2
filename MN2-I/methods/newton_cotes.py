# -*- coding: utf-8 -*-

def NC1Closed(partX,f):
    return ((partX[1]-partX[0])/2) * (f(partX[0]) + f(partX[1]))

def NC2Closed(partX,f):
    
    h = partX[1] - partX[0]
    
    return h/3*(f(partX[0]) + 4*f(partX[1]) + f(partX[2]))

def NC3Closed(partX,f):
    
    h = partX[1] - partX[0]

    return (3*(h)/8)*(f(partX[0]) + 3*f(partX[1]) + 3*f(partX[2]) + f(partX[3]))

def NC4Closed(partX,f):

     h = partX[1] - partX[0]

     return (2*h/45)*(7*f(partX[0]) + 32*f(partX[1]) + 12*f(partX[2]) + 32*f(partX[3]) + 7*partX[4])

def NC1Open(partX, f):
     h = partX[1] - partX[0]

     return (3*h/2)*(partX[0] + partX[1])

def NC2Open(partX, f):
    
    h = partX[1] - partX[0]

    return (4*h/3)*(2*f(partX[0]) - f(partX[1]) + 2*f(partX[2]))

def NC3Open(partX, f):
    
    h = partX[1] - partX[0]

    return (5*h/24)*(11*f(partX[0]) + f(partX[1]) + f(partX[2]) + 11*f(partX[3]))

def NC4Open(partX,f):

    h = partX[1] - partX[0] 

    return (6*h/20)*(11*f(partX[0]) - 14*f(partX[1]) + 26*f(partX[2]) - 14*f(partX[3]) + 11*f(partX[4]))