"""The code below was written by @author: https://github.com/DianaNtz and is an
implementation of the Runge Kutta method for the transport equation"""
import numpy as np
import matplotlib.pyplot as plt
import os
import imageio
#some initial values
filenames = []
nx=200
x0=-1
xfinal=1
h=(xfinal-x0)/(nx-1)
x=np.linspace(x0,xfinal,nx)

nt=120*1
t0=0
tfinal=0.5
dt=(tfinal-t0)/(nt-1)
#finite difference derivative
def first(D):
    n=len(D)
    Dr=np.zeros(n)
    Dr[0]=(D[0+1]-D[0])/(h)
    Dr[n-1]=(D[n-1]-D[n-1-1])/(h)
    for i in range(0,n-2):
        Dr[i+1]=(D[i+2]-D[i])/(2*h)
    return Dr


un=np.e**(-100*x**2/2)

