# -*- coding: utf-8 -*-
 
import pvi.methods as pvi
import math

F = lambda y,t : -4*y - 5*math.cos(t)

S0 = 3;

deltaT = 0.01

#nextS = pvi.range_kutta(S0,F,deltaT,0)
nextS2 = pvi.forward_euler(S0,F,deltaT,0)
nextS3 = pvi.range_kutta(S0,F,deltaT,0)
nextS4 = pvi.range_kutta(nextS3,F,deltaT,0)