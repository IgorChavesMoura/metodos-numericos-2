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
    
    if a == b:
        return 0
    
    while e > E:
        
        i1 = i2
        i2 = 0
        
        deltaX = (b-a)/n
        
        for k in range(n):
            
            partXi = a + (k*deltaX)
            partXf = a + ((k+1)*deltaX)
            
            partX = buildPartitionPoints(degree,partXi,partXf,isOpen)
            
            print(partX)
            
            i2 += calc(partX=partX,f=function)
        
            
        e = abs((i2 - i1)/i2)
        
        print('\n\n\n')
        
        n = n*2
        
    return i2

def integrate_mult(function,method,a,b,E):
    
    V1 = 0
    V2 = 0
    
    n = 1
    
    e = E + 1
    
    calc = method['calc']
    degree = method['degree']
    isOpen = method['isOpen']
    
    while e > E:
        
        V1 = V2
        V2 = 0
        
        
        deltaY = a/n
        
        for k in range(n):
            
            partY = a + k*deltaY
            
            y = lambda x: function(x,partY)
            
            V2 += integrate(y,method,0,partY,E)
            
            #partX = buildPartitionPoints(degree,partXi,partXf,isOpen)
            
        if V2 > 0:
            e = abs((V2 - V1)/V2)  
        
    
    
    return V2
        
    

def integrate_exp(function,method,expType,dexp,a,b,E):
    
    
    
    g = lambda alpha : function(expType(alpha,a,b))*dexp(alpha,a,b)
    
    C = 1
    deltaC = 0.1
    
    e = E+1
    
    
    
    while e > E:
        
        I1 = integrate(g,method,-C,C,E)
        
        C += deltaC
        
        I2 = integrate(g,method,-C,C,E)
        
        e = abs((I2-I1)/I2)
        
        I1 = I2
        
        
    return I2     

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






    

