# import math
# from solvers.euler import euler_step
# from solvers.runge_kutta import rk4_step
# def f(x):
#     return-x


# x_euler=1.0
# x_rk4=1.0
# h=0.1
# steps=20

# print("\tEuler\tRk4\tExact")

# for i in range(steps):
#     t=i*h
#     exact=math.exp(-t)##gives e power(-t),basic calculus.
    
#     print(f"{t:.2f}\t{x_euler:.5f}\t{x_rk4:.5f}\t{exact:.5f}")
#     x_euler=euler_step(f,x_euler,h)
#     x_rk4=rk4_step(f,x_rk4,h)
    
    

# ## To run lorenz
import numpy as np
from solvers.rk4_vector import rk4_step_vec
from systems.lorenz import lorenz

state=np.array([20.12,23.45,23.56],dtype=np.float64)
h = 0.0001
steps=30

trajectory=[]

for _ in range(steps):
    trajectory.append(state)
    state = rk4_step_vec(lorenz, state, h)

    if np.any(np.abs(state) > 1e6):
        print("State exploded, stopping early")
        break

trajectory = np.array(trajectory)
print("Simulation complete. Points:", trajectory.shape)
