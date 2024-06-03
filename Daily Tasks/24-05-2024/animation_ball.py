import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
height = 10  
g = 9.8  
e = 0.8  

# Time
dt = 0.1  # Time step
total_time = np.sqrt(2 * height / g) * 2  
steps = int(total_time / dt)  

# Ball properties
ball_radius = 0.5
ball_color = 'blue'

# Create figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(0, height + ball_radius)

# Initialize empty plot
ball, = ax.plot([], [], 'o', color=ball_color)

# Function to initialize the plot
def init():
    ball.set_data([], [])
    return ball,

# Function to update the plot
def update(frame):
    t = frame * dt
    # Calculate position using kinematic equation
    y = height - 0.5 * g * t ** 2
    if y < 0:
        y = 0
    # Update ball position
    ball.set_data([0], [y + ball_radius])
    return ball,

# Create animation
ani = FuncAnimation(fig, update, frames=range(steps), init_func=init, blit=True, interval=dt * 1000)

plt.title('Elastic Ball Animation')
plt.xlabel('X')
plt.ylabel('Y')

plt.gca().set_aspect('equal', adjustable='box')

plt.show()
