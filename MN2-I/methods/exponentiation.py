# -*- coding: utf-8 -*-

import math

def expSimple(alpha,a,b): 
    
    return (a+b)/2 + (((b-a)/2)*math.tanh(alpha))

def expDouble(alpha,a,b):
    
    return (a+b)/2 + (((b-a)/2)*math.tanh((math.pi/2)*math.sinh(alpha)))

def dSimple(alpha,a,b):
    
    return b-a/2*(math.cosh(alpha)**2)

def dDouble(alpha,a,b):
    
    return ((math.pi/4)*(b-a))*(math.cosh(alpha)/(math.cosh(math.pi/2*math.sinh(alpha)))**2)