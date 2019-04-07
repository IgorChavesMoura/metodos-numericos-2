# -*- coding: utf-8 -*-

from integrator import integrate
from integrator import integrate_exp
from integrator import integrate_mult
from methods import gauss_legendre as GL
from methods import newton_cotes as NC
from methods import exponentiation as EX

import functions
import math


method = {
        
    'calc':GL.GL3,
    'degree':3,
    'isOpen':False
    
}

f = lambda x,y : math.cos(x*y)

#I = integrate(functions.log3x,method,2,4,0.00001)

#M = integrate_mult(f,method,0,math.pi/2,0.001)



IEX = integrate_exp(functions.xTanX,method,EX.expSimple,EX.dSimple,0,(math.pi/2),0.00001)

