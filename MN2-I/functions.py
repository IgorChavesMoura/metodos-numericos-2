# -*- coding: utf-8 -*-

import math

def x(x):
    return x

def x2(x):
    return x*x

def x3(x):
    return x*x*x

def cos(x):
    return math.cos(x)

def sin(x):
    return math.sin(x)

def e(x):
    return math.exp(x)

def eminusx2(x):
    return math.exp(-1*(x*x))

def eminusx(x):
    return math.exp(-1*x)

def cbrtInv(x):
    return 1/x**(1./3.)

def sqrtInv(x):
    return 1/x**(1./2.)

def test_exp(x):
    
    if x==0:
        return 1
    
    return math.sqrt(1+(1/x))

def log3x(x):
    
    return (math.log(3*x))**5

def xTanX(x):
    
    return x/math.tan(x)