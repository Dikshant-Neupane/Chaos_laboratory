def rk4_step(f,x,h):
    """Performs one Runge-kutta 4th order step.
    f:The derivative function f(x)
    x:Current Value
    h:step size
    """
    k1=f(x)
    k2=f(x+0.5*h*k1)
    k3=f(x+0.5*h*k2)
    k4=f(x+h*k3)
    
    return x+(h/6)*(k1+2*k2+2*k3+k4)