
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