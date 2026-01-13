# Chaos Laboratory 🦋

Ever wondered how a butterfly flapping its wings in Brazil could theoretically cause a tornado in Texas? Well, this project won't answer that exactly, but it'll show you the math behind why that idea isn't completely crazy!

## What's This All About?

I built this to explore chaos theory through the famous Lorenz System - those beautiful butterfly-shaped plots you've probably seen in textbooks or on cool science posters. Back in 1963, Edward Lorenz stumbled upon something fascinating while trying to model weather patterns: tiny differences in starting conditions led to wildly different outcomes. He called it sensitive dependence on initial conditions, but we know it better as the **Butterfly Effect**.

## What Can It Do?

- Simulates the Lorenz attractor (that iconic butterfly shape)
- Uses proper numerical methods - I've implemented both Euler and Runge-Kutta 4th order solvers
- Shows the Butterfly Effect in action - watch two nearly identical starting points diverge dramatically
- Creates pretty 3D visualizations with a dark "chaos lab" aesthetic
- Modular code structure (because nobody likes spaghetti code)

## Libraries Used

This project keeps it simple with just two main libraries:

**NumPy** - The backbone for all numerical computations. It handles:
- Fast array operations for the 40,000+ time steps
- Vector math for the differential equations
- Computing distances between trajectories

**Matplotlib** - Creates all the visualizations:
- 3D plotting for the Lorenz butterfly attractor
- Standard 2D plots for the divergence analysis
- Custom styling for that dark theme aesthetic

Both are industry-standard libraries, well-documented, and battle-tested for scientific computing.

## Project Structure

```
chaos_laboratory/
├── main.py                 # Main simulation and visualization script
├── systems/
│   └── lorenz.py          # Lorenz system equations
├── solvers/
│   ├── euler.py           # Euler integration method
│   ├── runge_kutta.py     # RK4 integration method
│   └── rk4_vector.py      # Vectorized RK4 implementation
├── figures/               # Generated visualization outputs
│   ├── butterfly.png      # Lorenz attractor visualization
│   └── butterfly_effect.png # Sensitivity analysis plot
├── analysis/              # Analysis results and data
├── plan/                  # Project planning documents
└── Readme/                # Additional documentation
```

## How to Use This

### What You'll Need

Just Python 3.7 or newer, plus:
```bash
pip install numpy matplotlib
```

### Getting Started

Clone it and run it:
```bash
git clone https://github.com/Dikshant-Neupane/Chaos_laboratory.git
cd chaos_laboratory
python main.py
```

That's it! The script will crunch through the simulation and pop up two plots:
1. The mesmerizing Lorenz butterfly in 3D
2. A graph showing how two nearly identical starting points spiral off into completely different paths

The whole thing runs about 40,000 time steps (taking just a few seconds on a modern computer).

## The Math Behind It

The Lorenz system is just three differential equations, but boy do they create something complex:

```
dx/dt = σ(y - x)
dy/dt = x(ρ - z) - y
dz/dt = xy - βz
```

I'm using the classic chaotic parameters:
- σ (sigma) = 10.0
- ρ (rho) = 28.0  
- β (beta) = 8/3

These specific values put the system right in the chaotic regime where all the interesting stuff happens.

### Why the Butterfly Effect is Mind-Blowing

Here's the crazy part: I start two simulations with nearly identical conditions:
- Point 1: [0.1, 0.0, 0.0]
- Point 2: [0.100001, 0.0, 0.0]

That's a difference of just 0.00001 - like measuring something to the nearest millimeter and being off by the width of a human hair. Yet after running the simulation, these two points end up in completely different places. The distance between them grows exponentially, which you can see in the second plot that uses a log scale.

## A Bit About the Numerical Methods

I implemented two classic integration methods:

**Euler Method** - The simplest approach, basically just x(next) = x(now) + step_size × derivative. It works, but it's not super accurate for chaotic systems.

**Runge-Kutta 4th Order (RK4)** - This is the workhorse I actually use in the simulation. It's way more accurate because it samples the derivative at multiple points within each time step. The math looks scary but it's basically just being really careful about how we step forward in time:

```
k1 = f(x)
k2 = f(x + h·k1/2)
k3 = f(x + h·k2/2)
k4 = f(x + h·k3)
x(next) = x + (h/6)(k1 + 2k2 + 2k3 + k4)
```

RK4 gives us excellent accuracy without killing the computer - a sweet spot for this kind of simulation.

## The Visuals

You'll get two plots when you run this:

**The Lorenz Butterfly** - A 3D plot with about 38,000 points tracing out that iconic double-looped structure. I went with a dark background and cyan lines because, well, it looks cool and gives off proper "chaos laboratory" vibes.

**Divergence Plot** - This one shows how the distance between our two starting points grows over time. The y-axis is logarithmic because the growth is exponential - it would look like a vertical line on a normal scale!

## Want to Tweak Things?

The code is pretty straightforward to modify. You can:

**Change the chaos parameters** in main.py:
```python
def lorenz(state, sigma=10.0, rho=28.0, beta=8.0/3.0):
    # Try different values! Not all combinations are chaotic though
```

**Start from a different point**:
```python
state = np.array([0.1, 0.0, 0.0], dtype=np.float64)  # Change these
```

**Simulate longer** (or shorter):
```python
dt = 0.001          # Time step
steps = 40000       # How many steps
discard = 2000      # Throw away the first bit (transient behavior)
```

## Why Chaos Theory Matters

Chaos isn't just a fun math trick - it shows up everywhere in the real world:

**Weather** - This is literally why Lorenz discovered it. He was trying to model weather and realized long-term forecasting is fundamentally impossible beyond a certain point.

**Your heartbeat** - Healthy hearts actually have chaotic rhythms (too regular can indicate problems).

**Stock markets** - Those wild swings? Partially chaotic dynamics at play.

**Mixing fluids** - Why stirring your coffee creates those swirling patterns.

The wild thing is that these systems are completely deterministic - no randomness in the equations - yet they're practically unpredictable. That's the essence of chaos.

## Ideas for Future Improvements

If you want to contribute or extend this:
- Add other chaotic systems (Rössler attractor, Chen system, double pendulum)
- Calculate Lyapunov exponents (measures how "chaotic" a system is)
- Make an interactive version where you can adjust parameters in real-time
- Add Poincaré sections to visualize the strange attractor's structure
- Create bifurcation diagrams showing how behavior changes with parameters

Feel free to open a pull request!

## Some Cool References

If this got you interested in chaos theory:

- **"Chaos: Making a New Science"** by James Gleick - Super readable introduction, no heavy math required
- **"Nonlinear Dynamics and Chaos"** by Steven Strogatz - The textbook if you want to really dive deep
- Lorenz's original 1963 paper "Deterministic Nonperiodic Flow" - Short and surprisingly accessible

---

*"Chaos: When the present determines the future, but the approximate present does not approximately determine the future."* 
— Edward Lorenz (who has a way with words, clearly)