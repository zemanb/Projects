from numpy import *
import matplotlib.pyplot as plt
g = 9.8     # defining constants to be used in equations
l = 9.8   # pendulum length
gamma = .25
alpha_driving = .2  # will be varied later in the problem
dt = .01 # length of timesteps for the whole program
phase_frequency_squared = g/l
driving_frequency = sqrt(phase_frequency_squared - (2*(gamma**2)))
initial_velocity = 0    # initial conditions
initial_angle = pi/6
initial_angle2 = pi/6 + 0.001  # used to determine chaos in the pendulum, part 5
initial_time = 0
amplitude = alpha_driving/sqrt(((2*gamma*driving_frequency)**2) + ((phase_frequency_squared-(driving_frequency**2))**2))
analytical_phase = -arctan((2*gamma*driving_frequency)/(phase_frequency_squared - (driving_frequency**2)))  # analytical solution
print("The analytical amplitude is " + str(round(amplitude/pi, 2)) + "pi")  # displaying analytical solution
print("The analytical phase angle is " + str(round(analytical_phase/pi, 2)) + "pi radians")
print(driving_frequency)
angular_velocity = []  # empty arrays to be used in while loops, all variables which while be plotted, w is angular velocity
angle = []  # angle
d_angle = []   # absolute value of the change of the angle over time, used to show evidence of chaos
time = []

w = initial_velocity  # initializing variables
o = initial_angle
t = initial_time

while t <= 40:    # measuring angle and angular velocity over time until observed steady state
    angular_velocity.append(w)   # filling in arrays to plot later
    angle.append(o)
    time.append(t)
    sine_term = sin(driving_frequency * t)  # simplifying following equation

    def fo(o, w, t):   # functions for runge kutta method of finding angle and angular velocity
        return w

    def fw(o, w, t):
        return -2*gamma*w - g/l*o + alpha_driving*sine_term

    k1o = dt*fo(o, w, t)   # k values are parts of theta and omega equations, include values of the defined functions
    k1w = dt*fw(o, w, t)
    k2o = dt*fo(o + .5*k1o, w + .5*k1w, t + .5*dt)
    k2w = dt*fw(o + .5*k1o, w + .5*k1w, t + .5*dt)
    k3o = dt*fo(o + .5*k2o, w + .5*k2w, t + .5*dt)
    k3w = dt*fw(o + .5*k2o, w + .5*k2w, t + .5*dt)
    k4o = dt*fo(o + k3o, w + k3w, t + dt)
    k4w = dt*fw(o + k3o, w + k3w, t + dt)
    o += (1/6)*(k1o + (2*k2o) + (3*k3o) + k4o)  # change of angle and velocity each timestep
    w += (1/6)*(k1w + (2*k2w) + (3*k3w) + k4w)
    t += dt
    if o < -pi:  # these conditions keep the angle between -pi and pi
        o += pi*2
    elif o > pi:
        o -= pi*2

plt.plot(time, angular_velocity, 'g--', label="angular velocity")  # plotting angle and velocity over time, same color as they both model
plt.plot(time, angle, 'b:', label="angle")  # the linear differential equation
plt.xlabel('Time (s)')
plt.ylabel('Angle (rad) (...)/ Angular Velocity (rad/s) (---)')  # different units depending on plot style
plt.yticks(arange(-pi/4, 3*pi/8, pi/8), ["-pi/4", "-pi/8", "0", "pi/8", "pi/4"])  # easier to read
plt.title('Damped pendulum oscillation with a driving force')
plt.legend()
plt.show()


i = linspace(0.5, 1.4, 10)  # varied driving frequencies
df = []   # storing driving frequencies
ampsq = [] # used to plot amplitude squared and extract an estimated gamma value
phi = []  # plotting phase angle
for driving_frequency in i.round(1):
    angular_velocity.clear()  # empty arrays to be used in while loops, all variables which while be plotted, w is angular velocity
    angle.clear()  # new empty arrays
    time.clear()
    amp_angle = []   # empty arrays used to model amplitude squared an phase
    t_amp = []

    w = initial_velocity  # initializing variables
    o = initial_angle
    oA = initial_angle
    t = initial_time
    while t <= 40:  # measuring angle and angular velocity over time until observed steady state
        angular_velocity.append(w)  # filling in arrays to plot later
        angle.append(o)
        if t>28:     # only using steady-state portion of the plot to model amplitude and phase
            amp_angle.append(o)
            t_amp.append(t)
        time.append(t)
        sine_term = sin(driving_frequency * t)  # simplifying following equation


        def fo(o, w, t):   # same runge kutta process
            return w


        def fw(o, w, t):
            return -2 * gamma * w - g / l * o + alpha_driving * sine_term


        k1o = dt * fo(o, w, t)
        k1w = dt * fw(o, w, t)
        k2o = dt * fo(o + .5 * k1o, w + .5 * k1w, t + .5 * dt)
        k2w = dt * fw(o + .5 * k1o, w + .5 * k1w, t + .5 * dt)
        k3o = dt * fo(o + .5 * k2o, w + .5 * k2w, t + .5 * dt)
        k3w = dt * fw(o + .5 * k2o, w + .5 * k2w, t + .5 * dt)
        k4o = dt * fo(o + k3o, w + k3w, t + dt)
        k4w = dt * fw(o + k3o, w + k3w, t + dt)
        o += (1 / 6) * (k1o + (2 * k2o) + (3 * k3o) + k4o)
        w += (1 / 6) * (k1w + (2 * k2w) + (3 * k3w) + k4w)
        t += dt
        if o < -pi:  # these conditions keep the angle between -pi and pi
            o += pi * 2
        elif o > pi:
            o -= pi * 2
    plt.plot(time, angular_velocity, 'g--', label="angular velocity")  # 10 plots, one for each for loop iteration
    plt.plot(time, angle, 'b:', label="angle")
    plt.xlabel('Time (s)')
    plt.ylabel('Angle (rad) (...)/ Angular Velocity (rad/s) (---)')  # different units depending on plot style
    plt.yticks(arange(-pi / 4, 3 * pi / 8, pi / 8), ["-pi/4", "-pi/8", "0", "pi/8", "pi/4"])  # easier to read
    plt.title('Pendulum oscillation with driving frequency '+ str(driving_frequency) + ' s^-1') # differentiates the graphs
    plt.legend()
    plt.show()

    amplitude_squared = abs(amin(amp_angle))**2  # local minimum of theta in steady-state is the amplitude
    a = amp_angle.index(amin(amp_angle))
    tmin = t_amp[a]  # time at local minimum

    def phase(intg):  # finding the integer needed to find phase values for each frequency
        return 2*pi*intg + 1.5*pi - driving_frequency*tmin

    for x in range(-10, 25):
        if phase(x) < pi and phase(x) > -pi:
            p = phase(x)
    phi.append(p)
    ampsq.append(amplitude_squared)
    df.append(driving_frequency)
plt.plot(df, ampsq, 'b*')      # amplitude vs, frequency, used to estimate gamma value
plt.xlabel('Driving frequency (s^-1')
plt.ylabel('Amplitude Squared * pi/100 (rad^2)')
plt.yticks([0, .01*pi, .02*pi, .03*pi, .04*pi, .05*pi, .06*pi], ["0", "1", "2", "3", "4", "5", "6"])
plt.show()
plt.plot(df, phi, 'g>')   # phase vs frequency
plt.xlabel('Driving frequency (s^-1)')
plt.ylabel('Phase Angle (rad)')
plt.yticks([-pi, -3*pi/4, -pi/2, -pi/4, 0], ["-pi", "-3pi/4", "-pi/2", "-pi/4", "0"])
plt.show()

for alpha_driving in [0.2, 0.5, 1.2]: # similar to last for loop but varying alpha instead of frequency
    angular_velocity.clear()  # however, ODE is non linear, in omega equation theta is replaced with sin(theta)
    angle.clear()
    time.clear()
    driving_frequency = 2 / 3  # constant frequency, different from analytically calculated frequency
    w = initial_velocity
    o = initial_angle
    t = initial_time

    while t <= 40:
        angular_velocity.append(w)  # filling in arrays to plot later
        angle.append(o)
        time.append(t)

        sine_term = sin(driving_frequency * t)  # simplifying following equation


        def fo(o, w, t):  # runge kutta
            return w


        def fw(o, w, t):
            return -2 * gamma * w - sin(o)*g/l + alpha_driving * sine_term # this term makes equation non-linear, no more small angle approximation

        k1o = dt * fo(o, w, t)
        k1w = dt * fw(o, w, t)
        k2o = dt * fo(o + .5 * k1o, w + .5 * k1w, t + .5 * dt)
        k2w = dt * fw(o + .5 * k1o, w + .5 * k1w, t + .5 * dt)
        k3o = dt * fo(o + .5 * k2o, w + .5 * k2w, t + .5 * dt)
        k3w = dt * fw(o + .5 * k2o, w + .5 * k2w, t + .5 * dt)
        k4o = dt * fo(o + k3o, w + k3w, t + dt)
        k4w = dt * fw(o + k3o, w + k3w, t + dt)
        o += (1 / 6) * (k1o + (2 * k2o) + (3 * k3o) + k4o)
        w += (1 / 6) * (k1w + (2 * k2w) + (3 * k3w) + k4w)
        t += dt

        if o < -pi:  # these conditions keep the angle between -pi and pi
            o += pi * 2
        elif o > pi:
            o -= pi * 2

    if alpha_driving == 0.2:   # different plots for each alpha on the same graph
        plt.plot(angle, angular_velocity, 'k', label="0.2 rad/s^2")
    elif alpha_driving == 0.5:
        plt.plot(angle, angular_velocity, 'g', label="0.5 rad/s^2")
    else:
        plt.plot(angle, angular_velocity, 'r', label="1.2 rad/s^2")
plt.xlabel('Angle (rad)')
plt.ylabel('Angular Velocity (rad/s)')
plt.title('Non-linear Pendulum oscillation with varying driving acceleration')
plt.legend()
plt.show()

for alpha_driving in [0.2, 0.5, 1.2]:  # similar to last for loop, but the omega and theta equations our doubles
    angular_velocity.clear()   # o2 and w2 are just like o and w except for the initial angle, different by 0.001 rad
    angle.clear()
    d_angle.clear()   # change of angle
    time.clear()
    driving_frequency = 2 / 3
    w = initial_velocity
    w2 = initial_velocity  # initializing variables
    o = initial_angle
    o2 = initial_angle2  # here is the only difference between o and o2, which affects w and w2
    t = initial_time
    d_o = abs(o2-0)  # change of angle array, which is plotted later
    while t <= 40:
        angular_velocity.append(w)
        angle.append(o)
        time.append(t)
        d_angle.append(d_o)
        d_o = abs(o2 - o)
        sine_term = sin(driving_frequency * t)

        def fo2(o2, w2, t):  # replica of original runge kutta for o2 and w2
            return w2

        def fw2(o2, w2, t):
            return -2 * gamma * w2 - sin(g / l * o2) + alpha_driving * sine_term

        k1o2 = dt * fo2(o2, w2, t)
        k1w2 = dt * fw2(o2, w2, t)
        k2o2 = dt * fo2(o2 + .5 * k1o2, w2 + .5 * k1w2, t + .5 * dt)
        k2w2= dt * fw2(o2 + .5 * k1o2, w2 + .5 * k1w2, t + .5 * dt)
        k3o2 = dt * fo2(o2 + .5 * k2o2, w2 + .5 * k2w2, t + .5 * dt)
        k3w2 = dt * fw2(o2 + .5 * k2o2, w2 + .5 * k2w2, t + .5 * dt)
        k4o2 = dt * fo2(o2 + k3o2, w2 + k3w2, t + dt)
        k4w2 = dt * fw2(o2 + k3o2, w2 + k3w2, t + dt)
        o2 += (1 / 6) * (k1o2 + (2 * k2o2) + (3 * k3o2) + k4o2)
        w2 += (1 / 6) * (k1w2 + (2 * k2w2) + (3 * k3w2) + k4w2)

        def fo(o, w, t):
            return w

        def fw(o, w, t):
            return -2 * gamma * w - g/l*sin(o) + alpha_driving * sine_term

        k1o = dt * fo(o, w, t)
        k1w = dt * fw(o, w, t)
        k2o = dt * fo(o + .5 * k1o, w + .5 * k1w, t + .5 * dt)
        k2w = dt * fw(o + .5 * k1o, w + .5 * k1w, t + .5 * dt)
        k3o = dt * fo(o + .5 * k2o, w + .5 * k2w, t + .5 * dt)
        k3w = dt * fw(o + .5 * k2o, w + .5 * k2w, t + .5 * dt)
        k4o = dt * fo(o + k3o, w + k3w, t + dt)
        k4w = dt * fw(o + k3o, w + k3w, t + dt)
        o += (1 / 6) * (k1o + (2 * k2o) + (3 * k3o) + k4o)
        w += (1 / 6) * (k1w + (2 * k2w) + (3 * k3w) + k4w)
        t += dt

        if o < -pi:  # these conditions keep the angle between -pi and pi
            o += pi * 2
        elif o > pi:
            o -= pi * 2
        if o2 < -pi:  # these conditions keep the angle between -pi and pi
            o2 += pi * 2
        elif o2 > pi:
            o2 -= pi * 2

    if alpha_driving == 0.2: # plots for different alphas on the same graph
        plt.plot(time, d_angle, 'k', label="angle variation accel. 0.2") # change of angle vs time helps find lyapunov exponents
    elif alpha_driving == 0.5:
        plt.plot(time, d_angle, 'g', label="angle variation accel. 0.5")
    else:
        plt.plot(time, d_angle, 'r', label="angle variation accel. 1.2")
plt.xlabel('Time (s)')
plt.ylabel('Absolute Value of the change in Angle (rad)')
plt.title('Stability of Solutions over time')
plt.legend()
plt.yscale("log")  # plotting on log scale for better understandability, easier to find exponents
plt.show()


