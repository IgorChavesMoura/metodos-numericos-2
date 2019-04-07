# -*- coding: utf-8 -*-

#method -> json (dict) with a calc attr and a degree attr and a isOpen (philosophy) attr

def integrate(function,method,a,b,E):
    
    n = 1
    i1 = 0
    i2 = 0
    
    e = E+1
    
    calc = method['calc']
    degree = method['degree']
    isOpen = method['isOpen']
    
    
    while e > E:
        
        i1 = i2
        i2 = 0
        
        deltaX = (b-a)/n
        
        for k in range(n):
            
            partXi = a + (k*deltaX)
            partXf = a + ((k+1)*deltaX)
            
            partX = buildPartitionPoints(degree,partXi,partXf,isOpen)
            
            i2 += calc(partX=partX,f=function)
            
        e = abs((i2 - i1)/i2)
        
        n = n*2
        
    return i2

def integrateRK(F,method,a,b,E,S0):
    
    n = 1
    i1 = 0
    i2 = 0
    
    e = E+1
    
    calc = method['calc']
    degree = method['degree']

    
    
    while e > E:
        
        i1 = i2
        i2 = 0
        
        deltaX = (b-a)/n
        
        for k in range(n):
            
            partXi = a + (k*deltaX)
            partXf = a + ((k+1)*deltaX)
            
            partS,partT = buildPartitionPointsRK(degree,partXi,partXf,S0,F)
            
            i2 += calc(partS,partT,F=F)
            
        e = abs((i2 - i1)/i2)
        
        n = n*2
        
    return i2
    

def buildPartitionPoints(degree,xi,xf,isOpen):
        
    partX = []
    
    if isOpen:
        
        deltaX = (xf-xi)/(degree+2)
        
        for k in range(degree+1):
            partX[k] = (xi+deltaX) + k*deltaX
            
            
        
    else:
        
        deltaX = (xf-xi)/degree
        
        partX.append(xi)
        
        if degree > 1:
            
            for k in range(1,degree):
                
                partX.append(xi + k*deltaX)
        
        
        partX.append(xf)
        
    return partX   

def buildPartitionPointsRK(degree,ti,tf,S0,F):
    
    partS = []
    partT = []
    
    deltaT = (tf-ti)/degree
    
    partT.append(ti)
    partS.append(S0)
    
    if degree > 1:
        
        for k in range(1,degree):
            
            partT.append(ti + k*deltaT)
            partS.append(S0 + (ti + k*deltaT)*F(S0,ti))
        
    partT.append(tf)    
    partS.append(S0 + (tf)*F(S0,ti))

    return partS,partT

def NC1ClosedRK(partS,partT,F):
    return (((partT[1]-partT[0])/2) * (F(partS[0],partT[0]) + F(partS[1],partT[1])))


def NC2ClosedRK(partS,partT,F):
    
    h = partT[1] - partT[0]
    
    return h/3*(F(partS[0],partT[0]) + 4*F(partS[1],partT[1]) + F(partS[2],partT[2]))


def NC3ClosedRK(partS,partT,F):
    
    h = partT[1] - partT[0]
    
    return (3*h/8)*(F(partS[0],partT[0]) + 3*F(partS[1],partT[1]) + 3*F(partS[2],partT[2]) + F(partS[3],partT[3]))

def NC4ClosedRK(partS,partT,F):
    
    h = partT[1] - partT[0]
    
    return (2*h/45)*(7*F(partS[0],partT[0]) + 32*F(partS[1],partT[1]) + 12*F(partS[2],partT[2]) + 32*F(partS[3],partT[3]) + 7*(partS[4],partT[4]))

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

def GL2(partX,f):
    
    deltaX = partX[2] - partX[0]

   

    alpha = [ -0.5773502691896257 , 0.5773502691896257 ]
    w = [ 1, 1 ]

    I = 0;

    for i in range(2):

        I += w[i] * f(x(alpha[i],partX[0], partX[2]))



    

    I *= (deltaX / 2)

    return I

def GL3(partX,f):
    
    deltaX = partX[3] - partX[0];

    alpha = [ -0.7745966692414834, 0 , 0.7745966692414834 ];

    w = [ 0.5555555555555556, 0.8888888888888888 ,0.5555555555555556 ];

    I = 0

    for i in range(3):

        I += w[i] * f(x(alpha[i],partX[0], partX[3]));


    

    I *= (deltaX / 2)

    return I
    
def GL4(partX,f):
    
    deltaX = partX[4] - partX[0];

    alpha = [ -0.8611363115940526, -0.3399810435848563, 0.3399810435848563, 0.8611363115940526 ]

    w = [ 0.3478548451374538, 0.6521451548625461, 0.6521451548625461,  0.3478548451374538 ]

    I = 0

    for i in range(4):

        I += w[i] * f(x(alpha[i],partX[0], partX[4]))


    

    I *= (deltaX / 2)

    return I

def GL5(partX,f):
    
    deltaX = partX[5] - partX[0]

    I = 0

    alpha = [ -0.9061798459386640, -0.5384693101056831, 0.0000000000000000,  0.5384693101056831, 0.9061798459386640 ]

    w = [ 0.2369268850561891, 0.4786286704993665, 0.5688888888888889, 0.4786286704993665, 0.2369268850561891 ]

    for i in range(5):

        I += w[i] * f(x(alpha[i],partX[0], partX[5]))


    

    I *= (deltaX / 2)

    return I

def x(alpha,xi,xf):
    return ((xi + xf)/2) + (alpha*((xf-xi)/2))
    

def get_method_by_order(order):
    
    methods = {
                1:NC1ClosedRK,
                2:NC2ClosedRK,
                3:NC3ClosedRK,
                4:NC4ClosedRK
   }
    
    return methods[order]