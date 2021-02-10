from numpy import *
import matplotlib.pyplot as plt


def rsq(A):  # defining equations for analytical soln
    return A/pi


def bz_analytical(A, z, muI):
    return -(muI*rsq(A))/(2*((z**2)+rsq(A))**1.5)  # equation is negative so summation is counter clockwise


z = arange(-10, 10.1, .1)
plt.plot(z, bz_analytical(1, z, 8), 'k', label="Bz Analytical")  # analytical soln
n = .5   # limits of the square wire with current
MuI = 8   # used in magnetic field coefficient
field_x = []  # arrays for field components
field_y = []
field_z = []
value_z = []

for z in arange(-10, 10.1, .1):  # plotting components as function of z
    Bx = 0   # initialize components
    By = 0
    Bz = 0
    dz = 0
    for y in (array(range(-5, 6))/10):  # used to add up the field for the entire loop
        for x in (array(range(-5, 6))/10):
            r1 = array([x, y, 0])    # defining vectors used to find change in magnetic field
            r = array([0, 0, z])
            L = r - r1
            root_mag_L = L[0] ** 2 + L[1] ** 2 + L[2] ** 2
            mag_L_cubed = root_mag_L ** 1.5    # coefficient used in field calculation
            if mag_L_cubed == 0:   # avoid divide by 0 error
                mag_L_cubed += 0.0001
                C = MuI / (4 * pi) / mag_L_cubed # C is coefficient used to update magnetic field components
            else:
                C = MuI / (4 * pi) / mag_L_cubed
            if x == -n and y != -n:   # first quarter of the loop
                dx = 0
                dy = n / 5
                dr1 = array([dx, dy, dz])  # array for field equation
                cross = [(dr1[1]*L[2])-(dr1[2]*L[1]), -(dr1[0]*L[2])+(dr1[2]*L[0]), (dr1[0]*L[1])-(dr1[1]*L[0])]
                dBx = cross[0] * C   # change in each field component for one grid point
                dBy = cross[1] * C
                dBz = cross[2] * C
                Bx += dBx   # total magnetic field at current stage of iteration
                By += dBy
                Bz += dBz

            if y == n and x != -n: # 2nd quarter of loop, same process
                dx = n / 5
                dy = 0
                dr1 = array([dx, dy, dz])
                cross = [(dr1[1] * L[2]) - (dr1[2] * L[1]), -(dr1[0] * L[2]) + (dr1[2] * L[0]), (dr1[0] * L[1]) - (dr1[1] * L[0])]
                dBx = cross[0] * C
                dBy = cross[1] * C
                dBz = cross[2] * C
                Bx += dBx
                By += dBy
                Bz += dBz

            if x == n and y != n:  # 3rd q
                dx = 0
                dy = -n/5
                dr1 = array([dx, dy, dz])
                cross = [(dr1[1] * L[2]) - (dr1[2] * L[1]), -(dr1[0] * L[2]) + (dr1[2] * L[0]), (dr1[0] * L[1]) - (dr1[1] * L[0])]
                dBx = cross[0] * C
                dBy = cross[1] * C
                dBz = cross[2] * C
                Bx += dBx
                By += dBy
                Bz += dBz

            if y == -n and x != n: # 4th q
                dx = -n/5
                dy = 0
                dr1 = array([dx, dy, dz])
                cross = [(dr1[1] * L[2]) - (dr1[2] * L[1]), -(dr1[0] * L[2]) + (dr1[2] * L[0]), (dr1[0] * L[1]) - (dr1[1] * L[0])]
                dBx = cross[0] * C
                dBy = cross[1] * C
                dBz = cross[2] * C
                Bx += dBx
                By += dBy
                Bz += dBz

    field_x.append(Bx)  # field components from all 4 quarters have been added and are put in arrays
    field_y.append(By)  # 1 array component for each z value
    field_z.append(Bz)
    value_z.append(z)

plt.plot(value_z, field_z, 'r*', label="Bz")  # plotting z component vs z values, on same graph as analytical soln
plt.legend()
plt.xticks([-10, -5, 0, 5, 10])
plt.title("Z component of field, analytical vs numerical")
plt.xlabel("Z (m)")
plt.ylabel("Magnetic field (T)")
plt.show()
plt.plot(value_z, field_x, 'b*', label="Bx")  # x and y components vs z value on separate graph due to different axes
plt.plot(value_z, field_y, 'g*', label="By")
plt.legend()
plt.xticks([-10, -5, 0, 5, 10])
plt.title("X, Y components of field with x=y=0")
plt.xlabel("Z (m)")
plt.ylabel("Magnetic field (T)")
plt.show()

z = 1   # repeat entire first part but z remains constant
field_x.clear()
field_y.clear()
field_z.clear()
value_x = []  # for various x values, the current loop will iterate completely
for x1 in arange(-10, 10.1, .1): # same type of foor loop
    Bx = 0  # reset change in field components
    By = 0
    Bz = 0
    dz = 0
    for y in (array(range(-5, 6)) / 10):
        for x in (array(range(-5, 6)) / 10):
            r1 = array([x, y, 0])
            r = array([x1, 0, z]) # x1 is the x value that the current loop iterates completely for, z is constant
            L = r - r1
            root_mag_L = L[0] ** 2 + L[1] ** 2 + L[2] ** 2
            mag_L_cubed = root_mag_L ** 1.5
            if mag_L_cubed == 0:
                mag_L_cubed += 0.0001
                C = MuI / (4 * pi) / mag_L_cubed
            else:
                C = MuI / (4 * pi) / mag_L_cubed
            if x == -n and y != -n:  # same 4 quarter process
                dx = 0
                dy = n / 5
                dr1 = array([dx, dy, dz])
                cross = [(dr1[1] * L[2]) - (dr1[2] * L[1]), -(dr1[0] * L[2]) + (dr1[2] * L[0]),
                         (dr1[0] * L[1]) - (dr1[1] * L[0])]
                dBx = cross[0] * C
                dBy = cross[1] * C
                dBz = cross[2] * C
                Bx += dBx
                By += dBy
                Bz += dBz
            if y == n and x != -n:
                dx = n / 5
                dy = 0
                dr1 = array([dx, dy, dz])
                cross = [(dr1[1] * L[2]) - (dr1[2] * L[1]), -(dr1[0] * L[2]) + (dr1[2] * L[0]),
                         (dr1[0] * L[1]) - (dr1[1] * L[0])]
                dBx = cross[0] * C
                dBy = cross[1] * C
                dBz = cross[2] * C
                Bx += dBx
                By += dBy
                Bz += dBz

            if x == n and y != n:
                dx = 0
                dy = -n / 5
                dr1 = array([dx, dy, dz])
                cross = [(dr1[1] * L[2]) - (dr1[2] * L[1]), -(dr1[0] * L[2]) + (dr1[2] * L[0]),
                         (dr1[0] * L[1]) - (dr1[1] * L[0])]
                dBx = cross[0] * C
                dBy = cross[1] * C
                dBz = cross[2] * C
                Bx += dBx
                By += dBy
                Bz += dBz

            if y == -n and x != n:
                dx = -n / 5
                dy = 0
                dr1 = array([dx, dy, dz])
                cross = [(dr1[1] * L[2]) - (dr1[2] * L[1]), -(dr1[0] * L[2]) + (dr1[2] * L[0]),
                         (dr1[0] * L[1]) - (dr1[1] * L[0])]
                dBx = cross[0] * C
                dBy = cross[1] * C
                dBz = cross[2] * C
                Bx += dBx
                By += dBy
                Bz += dBz

    field_x.append(Bx)
    field_y.append(By)
    field_z.append(Bz)
    value_x.append(x1) # creates array of the various x values

plt.plot(value_x, field_z, 'r*', label="Bz") # z component vs x values
plt.legend()
plt.xticks([-10, -5, 0, 5, 10])
plt.title("Z component of field with y=0 z=1")
plt.xlabel("X (m)")
plt.ylabel("Magnetic field (T)")
plt.show()
plt.plot(value_z, field_x, 'b*', label="Bx")  # x, y components vs x values on same plot
plt.plot(value_z, field_y, 'g*', label="By")
plt.legend()
plt.xticks([-10, -5, 0, 5, 10])
plt.title("X, Y components of field with y=0 z=1")
plt.xlabel("X (m)")
plt.ylabel("Magnetic field (T)")
plt.show()

field_x.clear()
field_y.clear()
field_z.clear()
value_z.clear()

for z in arange(-10, 10.1, .1): # similar loop to the first part, components as function of z, with nonzero x
    Bx = 0
    By = 0
    Bz = 0
    dz = 0
    for y in (array(range(-5, 6))/10):
        for x in (array(range(-5, 6))/10):
            r1 = array([x, y, 0])
            r = array([0.5, 0, z]) # x and y are still constant, but x is nonzero
            L = r - r1
            root_mag_L = L[0] ** 2 + L[1] ** 2 + L[2] ** 2
            mag_L_cubed = root_mag_L ** 1.5
            if mag_L_cubed == 0:
                mag_L_cubed += 0.0001
                C = MuI / (4 * pi) / mag_L_cubed
            else:
                C = MuI / (4 * pi) / mag_L_cubed
            if x == -n and y != -n:
                dx = 0
                dy = n / 5
                dr1 = array([dx, dy, dz])
                cross = [(dr1[1]*L[2])-(dr1[2]*L[1]), -(dr1[0]*L[2])+(dr1[2]*L[0]), (dr1[0]*L[1])-(dr1[1]*L[0])]
                dBx = cross[0] * C
                dBy = cross[1] * C
                dBz = cross[2] * C
                Bx += dBx
                By += dBy
                Bz += dBz

            if y == n and x != -n:
                dx = n / 5
                dy = 0
                dr1 = array([dx, dy, dz])
                cross = [(dr1[1] * L[2]) - (dr1[2] * L[1]), -(dr1[0] * L[2]) + (dr1[2] * L[0]), (dr1[0] * L[1]) - (dr1[1] * L[0])]
                dBx = cross[0] * C
                dBy = cross[1] * C
                dBz = cross[2] * C
                Bx += dBx
                By += dBy
                Bz += dBz

            if x == n and y != n:
                dx = 0
                dy = -n/5
                dr1 = array([dx, dy, dz])
                cross = [(dr1[1] * L[2]) - (dr1[2] * L[1]), -(dr1[0] * L[2]) + (dr1[2] * L[0]), (dr1[0] * L[1]) - (dr1[1] * L[0])]
                dBx = cross[0] * C
                dBy = cross[1] * C
                dBz = cross[2] * C
                Bx += dBx
                By += dBy
                Bz += dBz

            if y == -n and x != n:
                dx = -n/5
                dy = 0
                dr1 = array([dx, dy, dz])
                cross = [(dr1[1] * L[2]) - (dr1[2] * L[1]), -(dr1[0] * L[2]) + (dr1[2] * L[0]), (dr1[0] * L[1]) - (dr1[1] * L[0])]
                dBx = cross[0] * C
                dBy = cross[1] * C
                dBz = cross[2] * C
                Bx += dBx
                By += dBy
                Bz += dBz

    field_x.append(Bx)
    field_y.append(By)
    field_z.append(Bz)
    value_z.append(z)

plt.plot(value_z, field_z, 'r*', label="Bz")  # z component vs z values
plt.legend()
plt.xticks([-10, -5, 0, 5, 10])
plt.title("Z component of field with x=0.5 y=0")
plt.xlabel("Z (m)")
plt.ylabel("Magnetic field (T)")
plt.show()
plt.plot(value_z, field_x, 'b*', label="Bx")  # x, y components vs z values
plt.plot(value_z, field_y, 'g*', label="By")
plt.legend()
plt.xticks([-10, -5, 0, 5, 10])
plt.title("X, Y components of field with x=0.5 y=0")
plt.xlabel("Z (m)")
plt.ylabel("Magnetic field (T)")
plt.ylim(0, 0.05)  # limits changed to not include outliers that would make the trends hard to visualize
plt.show()

