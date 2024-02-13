import numpy as np
import matplotlib.pyplot as plt


# Define and assign parameters
k = 0.1  # thermal conductivity
A = 1     # surface area
d = 0.1   # thickness of the solid
Te = 300  # temperature of the environment
T0 = 500  # initial temperature of the solid
dt = 0.01 # change in time 
tfinal = 100 # final time

# Function to calculate dQ/dt
def heat_transfer_rate(T):
    return -k * A * (T - Te) / d

# Simulation
time = np.arange(0, tfinal, dt)
T = np.zeros_like(time)
T[0] = T0  # initial temperature

for i in range(1, len(time)):
    dQdt = heat_transfer_rate(T[i-1])
    dT = dQdt * dt 
    T[i] = T[i-1] + dT

# Heat input
Q = k * A * (T - Te) * dt

# Calculate specific heat capacity (slope of the plot)
slope, _ = np.polyfit(Q, T, 1)
Cp_over_V = slope   # Assuming volume V is 1 (you need the volume to get Cp)
print("Specific heat capacity per unit volume (Cp/V):", Cp_over_V)

# Plotting time against temperature
plt.plot(time, T)
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.title('Temperature vs Time')
plt.grid(True)
plt.show()
