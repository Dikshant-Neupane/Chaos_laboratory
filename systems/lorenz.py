import numpy as np
def lorenz(state,sigma=10,rho=28,beta=8/3):
    x,y,z=state
    dx=sigma*(y-x)
    dy=x*(rho-z)-y
    dz=x*y-beta*z
    
    return np.array([dx,dy,dz])