def euler_step(f,x,h):
    """Perfomes one Euler integration step using formula
    x(n =1 (next step))=x(n)+h.f(x(n))
    where f= the ferivates function 
    x = current value
    h=step size
    The function returns next value afte rone euler steps.
    """
    return x+h*f(x)
