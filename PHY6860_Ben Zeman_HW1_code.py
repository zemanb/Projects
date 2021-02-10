from numpy import *
import matplotlib.pyplot as plt

half_life = 5700
tau = (-half_life/log(.5))   # decay constant
N_initial = (6.022E23*1E-15)/14  # number of particles when t = 0
t = linspace(0, 20000)    # times for each function
t_10 = []           # time variables for the 10, 100, and 1000 year timestep plots
t_100 = []          # empty arrays that will be filled in while loops
t_1000 = []
R_10 = []       # R is the negative derivative of N(t) with respect to t. It models particles activity
R_100 = []
R_1000 = []


def N(t):                 # N(t) is the number of particles at time t
    return N_initial * e ** (-t / tau)


def R(t):            # particle activity for the analytical solution
    return N(t)/tau


N_10_current = N_initial             # defining variables for timestep 10 solution
R_10_current = N_10_current/tau
time_10_current = 0
dt = 10
while time_10_current <= 20000:       # loop that records values for each timestep
    t_10.append(time_10_current)      # adding each value calculated to the t_10 and R_10 arrays
    R_10.append(R_10_current)

    N_10_current -= R_10_current * dt    # changing values of t_10 and R_10 in order to add a new value to each array
    time_10_current += dt
    R_10_current = N_10_current / tau


N_100_current = N_initial               # similar variables and while loop, except now for the timestep 100 solution
R_100_current = N_100_current/tau
time_100_current = 0
dt = 100
while time_100_current <= 20000:
    t_100.append(time_100_current)
    R_100.append(R_100_current)

    N_100_current -= R_100_current * dt
    time_100_current += dt
    R_100_current = N_100_current / tau


N_1000_current = N_initial            # similar variables and while loop, except now for the timestep 1000 solution
R_1000_current = N_1000_current/tau
time_1000_current = 0
dt = 1000
while time_1000_current <= 20000:
    t_1000.append(time_1000_current)
    R_1000.append(R_1000_current)

    N_1000_current -= R_1000_current * dt
    time_1000_current += dt
    R_1000_current = N_1000_current / tau


plt.plot(t, R(t), color='k', label="analytical solution", linewidth=6)  # plot of the analytical solution
plt.plot(t_10, R_10, 'bD', label="10y", markersize=3)  # plots of the three numerical solutions
plt.plot(t_100, R_100, 'm*', label="100y", markersize=4)  # markersizes and linewidths changed to make all plots visible
plt.plot(t_1000, R_1000, 'r>', label="1000y")   # different colors and markers to differentiate and show timesteps
plt.yscale('log')       # log scale on the y axis
plt.legend(loc='upper right')
plt.xlabel('Time (y)')             # labels for the graph
plt.ylabel('Particle Activity (log scale) (1/s)')
plt.yticks(arange(5E32, 35E32, 5E32), ['5E32', '1E33', '15E32', '2E33', '25E32', '30E33'])
plt.title('Activity of Carbon-14 isotope over 20000 years with varying time-steps')
plt.show()



