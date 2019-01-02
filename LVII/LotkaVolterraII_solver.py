# Lotka-Volterra model simulation
# Author: BIRICZ A
# Date: 22-24.10.2017

import numpy as np

# endpoints:
Ntimes = 100000
Tmin = 0
Tmax = 500
h = (Tmax-Tmin) / Ntimes
t = Tmin
# initialization:
y = np.empty( (2), dtype = float ) # container for prey y[0] and predator y[1]
y[0] = 0.1
y[1] = 5.0
a = 0.2 # prey growth rate
b = 0.1 # interaction rate between prey and predator
e = 1 # efficiency to convert prey to food
m = 0.1 # predator eating themselves
K = 20 # prey limit
#y[0] = m/(e*b)
#y[1] = a/b*( 1 - m/(e*b*K) )

def f( t, y, F ): # F is arbitrary function, but should be fitted to the RK4 solver
    F[0] = a*y[0]*( 1 - y[0]/K ) - b*y[0]*y[1]                 # RHS of 1st eq
    F[1] = e*b*y[0]*y[1] - m*y[1]               # RHS of 2nd eq

# -------------------------Start of RK4 solver--------------------------------
def rk4( t, y, h, Neqs ): # RK4 solver for arbitrary F; Neqs is the #eqs
    F = np.empty( (Neqs), dtype = float )
    ytemp = np.empty( (Neqs), dtype = float )
    k1 = np.empty( (Neqs), dtype = float )
    k2 = np.empty( (Neqs), dtype = float )
    k3= np.empty( (Neqs), dtype = float )
    k4 = np.empty( (Neqs), dtype = float )
    f( t, y, F ) # function evaluation at beginning point of the interval
    h2 = h*0.5
    for i in range( 0, Neqs ): # Euler-step
        k1[i] = h*F[i] # slope at the beginning of the interval using y
        ytemp[i] = y[i] + k1[i]*0.5
    f( t+h2, ytemp, F ) # function evaluation at midpoint
    for i in range( 0, Neqs ): # 2nd RK4-step
        k2[i] = h*F[i] # slope at the midpoint of the interval using y+0.5*k1
        ytemp[i] = y[i] + k2[i]*0.5
    f( t+h2, ytemp, F ) # function evaluation at midpoint
    for i in range( 0, Neqs ): # 3rd RK4-step
        k3[i] = h*F[i] # slope at the midpoint of the interval using y+0.5*k2
        ytemp[i] = y[i] + k3[i]
    f( t+h, ytemp, F ) # function evaluation at the end point of the interval
    for i in range( 0, Neqs ): # 4th RK4-step
        k4[i] = h*F[i] # slope at the end of the interval using y+h*k3
        y[i] = y[i] + ( k1[i] + 2*k2[i] + 2*k3[i] + k4[i] )*0.16666666666666666
# --------------------------End of RK4 solver---------------------------------

str1 = str(y[0]*10)
str1 = str1[:-2]
str2 = str(y[1]*10)
str2 = str2[:-2]
file = open( 'LVII_p'+str1+'_P'+str2+'.dat', 'w' ) # create file to write out
file.write("#time\tprey_t\tpredator_t\n")
i=0
while t < (Tmax):
    file.write( "%f %f %f\n" % (t, y[0], y[1]) )
    rk4( t, y, h, 2 ) # running the solver
    t += h
    i += 1
file.close
