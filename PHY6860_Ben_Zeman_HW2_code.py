from numpy import *                    # importing libraries
import matplotlib.pyplot as plt


magnitude_v_initial = 70           # defining all constants
air_density = 1.29
area = .0014
backspin = .25
g = 9.8
m = .046
x_initial = 0
y_initial = 0
dt = .01
c = .5
drag_coefficient = area / m

for angle in [pi/4, pi/6, pi/12, pi/20]:        # for loop creates plots of golf ball trajectory for 4 different angles
    x = []                  # empty arrays to be filled in while loop
    y = []
    velocity_x_initial = magnitude_v_initial * cos(angle)    # initializing variables that will be changed in loop
    velocity_y_initial = magnitude_v_initial * sin(angle)    # these variables help fill in arrays
    x_current = x_initial
    y_current = y_initial
    velocity_x = velocity_x_initial
    velocity_y = velocity_y_initial
    magnitude_v = sqrt(velocity_x**2 + velocity_y**2)

    while y_current >= 0:
        x.append(x_current)         # filling in x and y arrays
        y.append(y_current)

        x_current += velocity_x * dt       # updating coordinates of the ball after each timestep
        y_current += velocity_y * dt
        velocity_y -= g * dt

    x_final = x[-1]                      # priting total horizontal distance traveled by the ball
    print("The smooth ball hit at a " + str(int(angle * 180 / pi)) + " degree angle with no external force")
    print("travels " + str(round(x_final, 2)) + " meters horizontally before hitting the ground\n")

    if angle == pi/4:         # making plots with different titles and color labels for each initial angle
        plt.plot(x, y, 'k-', label="45 Degrees")
    elif angle == pi/6:
        plt.plot(x, y, 'r--', label="30 Degrees")
    elif angle == pi/12:
        plt.plot(x, y, 'b-.', label="15 Degrees")
    else:
        plt.plot(x, y, 'g:', label="9 Degrees")
plt.legend(loc='upper right')           # organization of the first graph, which has a plot for each initial angle
plt.xlabel('X Displacement  (m)')
plt.ylabel('Y Displacement  (m)')
plt.title('Projectile Motion of a smooth Golf Ball with no external forces')
plt.show()

for angle in [pi/4, pi/6, pi/12, pi/20]:   # same exact type of for loop, but now including drag force
    x_drag = []
    y_drag = []
    velocity_x_initial = magnitude_v_initial * cos(angle)
    velocity_y_initial = magnitude_v_initial * sin(angle)
    x_current = x_initial
    y_current = y_initial
    velocity_x = velocity_x_initial
    velocity_y = velocity_y_initial
    magnitude_v = sqrt(velocity_x ** 2 + velocity_y ** 2)

    while y_current >= 0:
        x_drag.append(x_current)
        y_drag.append(y_current)

        x_current += velocity_x * dt
        y_current += velocity_y * dt
        magnitude_v = sqrt(velocity_x ** 2 + velocity_y ** 2)
        drag_force_x = c * air_density * magnitude_v * velocity_x * drag_coefficient # these equations update because
        drag_force_y = c * air_density * magnitude_v * velocity_y * drag_coefficient # velocity changes each time
        velocity_x -= drag_force_x * dt  # velocity equations are different, making displacement equations
        velocity_y -= (g + drag_force_y) * dt  # different from the first loop even though they look the same

    x_drag_final = x_drag[-1]
    print("The smooth ball hit at a " + str(int(angle * 180 / pi)) + " degree angle with only drag force")
    print("travels " + str(round(x_drag_final, 2)) + " meters horizontally before hitting the ground\n")

    if angle == pi/4:
        plt.plot(x_drag, y_drag, 'k-', label="45 Degrees")
    elif angle == pi/6:
        plt.plot(x_drag, y_drag, 'r--', label="30 Degrees")
    elif angle == pi/12:
        plt.plot(x_drag, y_drag, 'b-.', label="15 Degrees")
    else:
        plt.plot(x_drag, y_drag, 'g:', label="9 Degrees")
plt.legend(loc='upper right')
plt.xlabel('X Displacement  (m)')
plt.ylabel('Y Displacement  (m)')
plt.title('Projectile Motion of a smooth Golf Ball with drag force accounted for')
plt.show()

for angle in [pi/4, pi/6, pi/12, pi/20]:  # same as first loop, but now for a dimpled ball with drag force

    x_dimples = []
    y_dimples = []
    velocity_x_initial = magnitude_v_initial * cos(angle)
    velocity_y_initial = magnitude_v_initial * sin(angle)
    x_current = x_initial
    y_current = y_initial
    velocity_x = velocity_x_initial
    velocity_y = velocity_y_initial

    while y_current >= 0:
        x_dimples.append(x_current)
        y_dimples.append(y_current)
        magnitude_v = sqrt(velocity_x ** 2 + velocity_y ** 2) # needed inside the loop as c depends on magnitude of v

        if magnitude_v <= 14:  # c is still included in drag force but is no longer a constant
            c = .5
        else:
            c = 7 / magnitude_v

        x_current += velocity_x * dt
        y_current += velocity_y * dt
        drag_force_x = c * air_density * magnitude_v * velocity_x * drag_coefficient  # uses the variable c
        drag_force_y = c * air_density * magnitude_v * velocity_y * drag_coefficient  # but otherwise the same
        velocity_x -= drag_force_x * dt
        velocity_y -= (g + drag_force_y) * dt

    x_dimples_final = x_dimples[-1]
    print("The dimpled ball hit at a " + str(int(angle * 180 / pi)) + " degree angle with only the drag force")
    print("travels " + str(round(x_dimples_final, 2)) + " meters horizontally before hitting the ground\n")

    if angle == pi/4:
        plt.plot(x_dimples, y_dimples, 'k-', label="45 Degrees")
    elif angle == pi/6:
        plt.plot(x_dimples, y_dimples, 'r--', label="30 Degrees")
    elif angle == pi/12:
        plt.plot(x_dimples, y_dimples, 'b-.', label="15 Degrees")
    else:
        plt.plot(x_dimples, y_dimples, 'g:', label="9 Degrees")
plt.legend(loc='upper right')
plt.xlabel('X Displacement  (m)')
plt.ylabel('Y Displacement  (m)')
plt.title('Projectile Motion of a dimpled Golf Ball with drag force accounted for')
plt.show()

for angle in [pi/4, pi/6, pi/12, pi/20]:  # this loop is just like the last one but adds backspin
    x_complete = []
    y_complete = []
    velocity_x_initial = magnitude_v_initial * cos(angle)
    velocity_y_initial = magnitude_v_initial * sin(angle)
    x_current = x_initial
    y_current = y_initial
    velocity_x = velocity_x_initial
    velocity_y = velocity_y_initial

    while y_current >= 0:
        x_complete.append(x_current)
        y_complete.append(y_current)

        magnitude_v = sqrt(velocity_x ** 2 + velocity_y ** 2)

        if magnitude_v <= 14:
            c = .5
        else:
            c = 7 / magnitude_v

        x_current += velocity_x * dt
        y_current += velocity_y * dt
        drag_force_x = c * air_density * magnitude_v * velocity_x * drag_coefficient
        drag_force_y = c * air_density * magnitude_v * velocity_y * drag_coefficient
        magnus_force_x = backspin * velocity_y  # the force from the spin which adjust velocity equations
        magnus_force_y = backspin * velocity_x  # x and y velocities are no longer independent of each other
        velocity_x -= (drag_force_x + magnus_force_x) * dt
        velocity_y -= (g + drag_force_y - magnus_force_y) * dt

    x_complete_final = x_complete[-1]
    print("The dimpled ball hit at a " + str(int(angle * 180 / pi)) + " degree angle with drag and calculated spin")
    print("travels " + str(round(x_drag_final, 2)) + " meters horizontally before hitting the ground\n")

    if angle == pi / 4:
        plt.plot(x_complete, y_complete, 'k-', label="45 Degrees")
    elif angle == pi / 6:
        plt.plot(x_complete, y_complete, 'r--', label="30 Degrees")
    elif angle == pi / 12:
        plt.plot(x_complete, y_complete, 'b-.', label="15 Degrees")
    else:
        plt.plot(x_complete, y_complete, 'g:', label="9 Degrees")
plt.legend(loc='upper right')
plt.xlabel('X Displacement  (m)')
plt.ylabel('Y Displacement  (m)')
plt.title('Projectile Motion of a dimpled Golf Ball with drag and spin accounted for')
plt.show()

















