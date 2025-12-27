import math
from solvers.euler import euler_step
def f(x):
    return-x

x=1.0
h=0.1
steps=20

print("\tEuler\t\Exact")

for i in range(steps):
    t=i*h
    exact=math.exp(-t)
    print(f"{t:.2f}\t{x:.5f}\t{exact:.5f}")
    x=euler_step(f,x,h)