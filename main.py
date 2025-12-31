import math
from solvers.euler import euler_step
from solvers.runge_kutta import rk4_step
def f(x):
    return-x


x_euler=1.0
x_rk4=1.0
h=0.1
steps=20

print("\tEuler\tRk4\tExact")

for i in range(steps):
    t=i*h
    exact=math.exp(-t)##gives e power(-t),basic calculus.
    
    print(f"{t:.2f}\t{x_euler:.5f}\t{x_rk4:.5f}\t{exact:.5f}")
    x_euler=euler_step(f,x_euler,h)
    x_rk4=rk4_step(f,x_rk4,h)