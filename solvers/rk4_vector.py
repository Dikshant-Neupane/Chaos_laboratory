import numpy as np
def rk4_step_vec(f, state, h):
    '''RK$ step for vector-valued systems.
    f:function(state)
    state:numpy array[x,y,x]
    h:step size'''
    k1 = f(state)
    k2 = f(state + 0.5 * h * k1)
    k3 = f(state + 0.5 * h * k2)
    k4 = f(state + h * k3)
    return state + (h / 6.0) * (k1 + 2*k2 + 2*k3 + k4)




   