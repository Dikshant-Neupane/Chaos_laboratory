import numpy as np
import matplotlib.pyplot as plt

# Lorenz System (Standard Chaotic Parameters)

def lorenz(state, sigma=10.0, rho=28.0, beta=8.0/3.0):
    x, y, z = state

    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z

    return np.array([dx, dy, dz], dtype=np.float64)


# Runge–Kutta 4th Order Integrator (RK4)

def rk4_step(f, state, h):
    k1 = f(state)
    k2 = f(state + 0.5 * h * k1)
    k3 = f(state + 0.5 * h * k2)
    k4 = f(state + h * k3)

    return state + (h / 6.0) * (k1 + 2*k2 + 2*k3 + k4)


# Simulation Parameters (Optimized)

dt = 0.001
steps = 40000      
discard = 2000     

state = np.array([0.1, 0.0, 0.0], dtype=np.float64)
trajectory = []

# Run Simulation

for i in range(steps):
    state = rk4_step(lorenz, state, dt)

    if np.any(np.abs(state) > 1e6):
        print("Numerical instability detected. Stopping.")
        break

    if i > discard:
        trajectory.append(state)

trajectory = np.array(trajectory)
print("Simulation complete. Points:", trajectory.shape[0])



# Plot Lorenz Butterfly 

fig = plt.figure(figsize=(9, 7))
ax = fig.add_subplot(111, projection="3d")

ax.plot(
    trajectory[:, 0],
    trajectory[:, 1],
    trajectory[:, 2],
    color="cyan",
    lw=0.4
)

ax.set_title("Lorenz Butterfly – Chaos Laboratory", fontsize=14)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

# Correct 3D proportions
ax.set_box_aspect([1, 1, 1])


# Dark Chaos Lab Theme

ax.set_facecolor("black")
fig.patch.set_facecolor("black")

ax.xaxis.label.set_color("white")
ax.yaxis.label.set_color("white")
ax.zaxis.label.set_color("white")
ax.title.set_color("white")
ax.tick_params(colors="white")

plt.tight_layout()
plt.show()




##Butteryfly Effect
state1=np.array([0.1,0.0,0.0],dtype=np.float64)
state2=np.array([0.100001,0.0,0.0],dtype=np.float64)

step=15000
distance=[]
time=[]

for i in range(steps):
    state1=rk4_step(lorenz,step,dt)
    state2=rk4_step(lorenz,state2,dt)
    
    d=np.linalg.norm(state1 -state2)
    distance.append(d)
    time.append(i*dt)
    
plt.figure(figure=(8,5))
plt.plot(time,distance,color="orange")
plt.yscale("log")
plt.xlabel("Time")
plt.ylabel("DIstance between trajectories(log scale)")
plt.title("Butterfly Efect:Sensitivity to Inital Conditions")
plt.grid(True)
plt.tight_layout()
plt.show()     