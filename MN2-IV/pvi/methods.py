#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pvi.integrator as integrator


def forward_euler(S,F,deltaT,t):
    
    nextS = S + deltaT*F(S,t)
    
   
    
    return nextS
    
def range_kutta(S,F,deltaT,t,order=1):
    
    integration_method = integrator.get_method_by_order(order)
    
    method = {
        
        'calc':integration_method,
        'degree':order           
                
    }
    
    nextS = S + integrator.integrateRK(F,method,t,(t+deltaT),0.001,S)
    
    return nextS


#def predictor_corrector(previousS, F, deltaT, t, points=2, i):
    
    