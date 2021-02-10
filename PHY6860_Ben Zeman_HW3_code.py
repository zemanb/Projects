from numpy import *
import matplotlib.pyplot as plt
g = 9.8     # defining constants to be used in equations
l = 9.8   # pendulum length
gamma = .25
alpha_driving = .2
dt = .01
phase_frequency_squared = g/l
driving_frequency = sqrt(phase_frequency_squared - (2*(gamma**2)))
initial_velocity = 0    # initial conditions
initial_angle = pi/6
initial_angle2 = pi/6 + 0.001
initial_time = 0
amplitude = alpha_driving/sqrt(((2*gamma*driving_frequency)**2) + ((phase_frequency_squared-(driving_frequency**2))**2))
phase = -arctan((2*gamma*driving_frequency)/(phase_frequency_squared - (driving_frequency**2)))  # analytical solution
print("The analytical amplitude is " + str(round(amplitude/pi, 2)) + "pi")  # displaying analytical solution
print("The analytical phase angle is " + str(round(phase/pi, 2)) + "pi radians")
print(driving_frequency)
w = []  # empty arrays to be used in while loops, all variables which while be plotted, w is angular velocity
o = []  # angle
d_o = []   # absolute value of the change of the angle over time, used to show evidence of chaos
t = []

angular_velocity = initial_velocity  # initializing variables
angle = initial_angle
time = initial_time

while time <= 22:    # measuring angle and angular velocity over time until observed steady state
    w.append(angular_velocity)   # filling in arrays to plot later
    o.append(angle)
    t.append(time)
    sine_term = sin(driving_frequency * time)  # simplifying following equation
    angular_velocity = angular_velocity-2*gamma*angular_velocity*dt-g/l*angle*dt+alpha_driving*sine_term*dt
    angle += angular_velocity*dt  # these functions will input values into arrays to plot
    time += dt
    if angle < -pi:  # these conditions keep the angle between -pi and pi
        angle += pi*2
    elif angle > pi:
        angle -= pi*2

plt.plot(t, w, 'k--', label="velocity linear")  # plotting angle and velocity over time, same color as they both model
plt.plot(t, o, 'k:', label="angle linear")  # the linear differential equation


for alpha_driving in [0.2, 1.2]:  # repeating while loop for different driving accelerations
    w.clear() # clearing arrays to refill
    o.clear()
    t.clear()
    angular_velocity = initial_velocity
    angle = initial_angle
    time = initial_time

    while time <= 22: # same as previous while loop, but replacing sin(angle) for angle to calculate velocity
        w.append(angular_velocity)  # makes equation nonlinear
        o.append(angle)
        t.append(time)
        sine_term = sin(driving_frequency * time)
        angular_velocity = angular_velocity-2*gamma*angular_velocity*dt-g/l*sin(angle)*dt+alpha_driving*sine_term*dt
        angle += angular_velocity*dt
        time += dt
        if angle < -pi:
            angle += pi * 2
        elif angle > pi:
            angle -= pi * 2

    if alpha_driving == 0.2:  # different plots for different accelerations
        plt.plot(t, w, 'g-.', label="velocity nonlinear accel. 0.2")  # same color as they both are nonlinear equations
        plt.plot(t, o, 'g:', label="angle nonlinear accel. 0.2")
    else:
        plt.plot(t, w, 'r--', label="velocity nonlinear accel. 1.2")
        plt.plot(t, o, 'r:', label="theta nonlinear accel. 1.2")
plt.xlabel('Time (s)')
plt.ylabel('Angle (rad) (...)/ Angular Velocity (rad/s) (---)')  # different units depending on plot style
plt.yticks(arange(-pi*3/4, pi, pi/4), ["-3/4pi", "-pi/2", "-pi/4", "0", "pi/4", "pi/2", "3/4pi"])  # easier to read
plt.title('Damped pendulum oscillation with a driving force')
plt.xlim(0, 22)  # no white space before or after plots
plt.legend(prop={'size': 5})
plt.show()

for alpha_driving in [0.2, 0.5, 1.2]:  # same as previous for loop but for 3 accelerations
    d_o.clear()  # not filling velocity and angle as they aren't needed to plot
    t.clear()
    angular_velocity = initial_velocity
    angular_velocity2 = initial_velocity  # velocity2 and angle2 to be compared to velocity1 and angle2
    angle = initial_angle # this will generate change of angle values
    angle2 = initial_angle2
    time = initial_time
    driving_frequency = 2/3  # using a different frequency

    while time <= 24:
        d_angle = absolute(angle - angle2)
        d_o.append(d_angle)  # appending new array which had not been used yet
        t.append(time)
        sine_term = sin(driving_frequency * time)
        angular_velocity = angular_velocity-2*gamma*angular_velocity*dt-g/l*sin(angle)*dt+alpha_driving*sine_term*dt
        angle += angular_velocity * dt
        angular_velocity2 = angular_velocity2-2*gamma*angular_velocity2*dt-g/l*sin(angle2)*dt+alpha_driving*sine_term*dt
        angle2 += angular_velocity2 * dt  # same equations as before just doubled
        time += dt

    if alpha_driving == 0.2:
        plt.plot(t, d_o, 'k', label="angle variation accel. 0.2")
    elif alpha_driving == 0.5:
        plt.plot(t, d_o, 'g', label="angle variation accel. 0.5")
    else:
        plt.plot(t, d_o, 'r', label="angle variation accel. 1.2")
plt.xlabel('Time (s)')
plt.ylabel('Absolute Value of the change in Angle (rad)')
plt.title('Stability of Solutions over time')
plt.legend()
plt.yscale("log")  # plotting on log scale for better understandability
plt.show()





