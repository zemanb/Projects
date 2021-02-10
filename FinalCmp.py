import numpy as np
import matplotlib.pyplot as plt
import math
n = 50
e = 2.71828
  # empty arrays
ispin = np.zeros((n, n))
energy = np.zeros((n, n))
d_energy = np.zeros((n, n))
  # defining constants
N = n**2
J = 1.5
m = []  # arrays used for counts in graphs later
t = []
c = []
logn = []
grid = []
cmax = []
M_list = []
P = 50
Nm = 100  # parameters adjusted for accurate results
tmin = 1
tmax = 11
tstep = 1
for i in range(n):
    for j in range(n):
        ispin[i, j] = np.random.randint(100)  # random simulator to generate a lattice of spins, up or down, 1 or -1
        if ispin[i, j] < P:
            ispin[i, j] = 1
        else:
            ispin[i, j] = -1
for T in np.arange(tmin, tmax + tstep, tstep): # varying temperature to find critical temp with magnetization
    print(T)
    M_list.clear()
    spin = np.zeros((n, n))  # empty arrays to help calculate magnetization
    energy = np.zeros((n, n))
    d_energy = np.zeros((n, n))
    sum_M = 0
    for i in range(n):
        for j in range(n):
            spin[i, j] = ispin[i, j]  # same initial lattice used for each temperature
    for b in range(Nm):  #  number of Monte-Carlo iterations to reach equilibrium
        for i in range(n):
            for j in range(n):  # assigning energies to each point based on spin of point and neighbors
                if i == 0 and j != 0 and j != n - 1:
                    energy[i, j] = -J * spin[i, j] * (spin[i + 1, j] + spin[n - 1, j] + spin[i, j + 1] + spin[i, j - 1])
                if i != 0 and j == 0 and i != n - 1:
                    energy[i, j] = -J * spin[i, j] * (spin[i + 1, j] + spin[i - 1, j] + spin[i, j + 1] + spin[i, n - 1])
                if i == n - 1 and j != 0 and j != n - 1:
                    energy[i, j] = -J * spin[i, j] * (spin[0, j] + spin[i - 1, j] + spin[i, j + 1] + spin[i, j - 1])
                if i != 0 and j == n - 1 and i != n - 1:
                    energy[i, j] = -J * spin[i, j] * (spin[i + 1, j] + spin[i - 1, j] + spin[i, 0] + spin[i, j - 1])
                if i == 0 and j == 0:
                    energy[i, j] = -J * spin[i, j] * (spin[i + 1, j] + spin[n - 1, j] + spin[i, j + 1] + spin[i, n - 1])
                if i == 0 and j == n - 1:
                    energy[i, j] = -J * spin[i, j] * (spin[i + 1, j] + spin[n - 1, j] + spin[i, 0] + spin[i, j - 1])
                if i == n - 1 and j == 0:
                    energy[i, j] = -J * spin[i, j] * (spin[0, j] + spin[i - 1, j] + spin[i, j + 1] + spin[i, n - 1])
                if i == n - 1 and j == n - 1:
                    energy[i, j] = -J * spin[i, j] * (spin[0, j] + spin[i - 1, j] + spin[i, 0] + spin[i, j - 1])
                if i != 0 and j != 0 and i != n - 1 and j != n - 1:
                    energy[i, j] = -J * spin[i, j] * (spin[i + 1, j] + spin[i - 1, j] + spin[i, j + 1] + spin[i, j - 1])
        for i in range(n):
            for j in range(n):
                d_energy[i, j] = -2 * energy[i, j]  # change of energy if spin is flipped
                if d_energy[i, j] < 0:
                    spin[i, j] *= -1 #  flipping the spin
                if d_energy[i, j] > 0:
                    r = np.round(np.random.uniform(0, 1.00001), 5)  # deciding whether to flip the spin
                    ex = (-d_energy[i, j]) / T
                    if r <= e **(ex):
                        spin[i, j] *= -1
        M = 0
        for i in range(n):
            for j in range(n):
                M += spin[i, j]  # total magnetization for each microstate
    # print(M)
        sum_M += M
    # print(spin)
    m.append(abs(sum_M/Nm))  # total magnetization of system
    # m.append(sum_M)
    t.append(T)
plt.plot(t, m)  # plotting to find critical temp
plt.title("Magnetization vs temperature, temp step " + str(tstep) + " kT")
plt.xlabel("Temperature (kT)")
plt.ylabel("Magnetization")
plt.show()
for n in [5, 10, 15, 20, 30, 50, 75, 100, 200, 500]: #  will plot specific heat vs temp for various grid sizes
    spin = np.zeros((n, n))  #  reinitializing arrays
    ispin = np.zeros((n, n))
    energy = np.zeros((n, n))
    d_energy = np.zeros((n, n))
    c.clear()
    t.clear()
    N = n ** 2
    for i in range(n):
        for j in range(n):
            ispin[i, j] = np.random.randint(100)  # random simulator to generate a lattice
            if ispin[i, j] < P:
                ispin[i, j] = 1
            else:
                ispin[i, j] = -1
    for T in np.arange(tmin, tmax + tstep, tstep):  # similar to first part
        M_list.clear()
        sum_energy = 0
        sum_energy2 = 0
        spin = np.zeros((n, n))
        energy = np.zeros((n, n))
        d_energy = np.zeros((n, n))
        sum_M = 0
        for i in range(n):
            for j in range(n):
                spin[i, j] = ispin[i, j]
        for b in range(Nm):
            for i in range(n):
                for j in range(n):
                    if i == 0 and j != 0 and j != n - 1:
                        energy[i, j] = -J * spin[i, j] * (
                                    spin[i + 1, j] + spin[n - 1, j] + spin[i, j + 1] + spin[i, j - 1])
                    if i != 0 and j == 0 and i != n - 1:
                        energy[i, j] = -J * spin[i, j] * (
                                    spin[i + 1, j] + spin[i - 1, j] + spin[i, j + 1] + spin[i, n - 1])
                    if i == n - 1 and j != 0 and j != n - 1:
                        energy[i, j] = -J * spin[i, j] * (spin[0, j] + spin[i - 1, j] + spin[i, j + 1] + spin[i, j - 1])
                    if i != 0 and j == n - 1 and i != n - 1:
                        energy[i, j] = -J * spin[i, j] * (spin[i + 1, j] + spin[i - 1, j] + spin[i, 0] + spin[i, j - 1])
                    if i == 0 and j == 0:
                        energy[i, j] = -J * spin[i, j] * (
                                    spin[i + 1, j] + spin[n - 1, j] + spin[i, j + 1] + spin[i, n - 1])
                    if i == 0 and j == n - 1:
                        energy[i, j] = -J * spin[i, j] * (spin[i + 1, j] + spin[n - 1, j] + spin[i, 0] + spin[i, j - 1])
                    if i == n - 1 and j == 0:
                        energy[i, j] = -J * spin[i, j] * (spin[0, j] + spin[i - 1, j] + spin[i, j + 1] + spin[i, n - 1])
                    if i == n - 1 and j == n - 1:
                        energy[i, j] = -J * spin[i, j] * (spin[0, j] + spin[i - 1, j] + spin[i, 0] + spin[i, j - 1])
                    if i != 0 and j != 0 and i != n - 1 and j != n - 1:
                        energy[i, j] = -J * spin[i, j] * (
                                    spin[i + 1, j] + spin[i - 1, j] + spin[i, j + 1] + spin[i, j - 1])
            for i in range(n):
                for j in range(n):
                    d_energy[i, j] = -2 * energy[i, j]

                    if d_energy[i, j] < 0:
                        spin[i, j] *= -1
                    if d_energy[i, j] > 0:
                        r = np.round(np.random.uniform(0, 1.00001), 5)
                        ex = (-d_energy[i, j]) / T
                        if r <= e**(ex):
                            spin[i, j] *= -1
            mstate_energy = 0  # counting the energy of the microstate
            for i in range(n):
                for j in range(n):
                    mstate_energy += energy[i, j]
            sum_energy += mstate_energy # sum of energies of all the microstates
            sum_energy2 += (mstate_energy ** 2)
        avg_E = sum_energy / Nm  # average energies per microstate
        avg_E2 = sum_energy2 / Nm
        dE_specific = avg_E2 - (avg_E ** 2)  # the average variation in energy, squared

        C = dE_specific / (T**2)  # specific heat for each temperature
        c.append(C / N)  # comparing specific heat per grid point with temperature
        t.append(T)

    if n == 5 or n == 15 or n == 30 or n == 100 or n == 500:  # plotting relationship for 5 different grid sizes
        plt.plot(t, c)
        plt.title("Specific Heat vs temperature with a " + str(n) + " X " + str(n) + " grid of spins")
        plt.xlabel("Temperature (kT)")
        plt.ylabel("Specific Heat per grid point")

    grid.append(n)
    logn.append(math.log(n))
    cmax.append(max(c))  # finding the maximum specific heat per grid point
    plt.show()
plt.plot(grid, cmax, 'b*')  # max specific heat per grid point vs number of grid points
plt.title("Maximum specific heat per grid size vs grid size")
plt.xlabel("grid points in each dimension")
plt.ylabel("Specific heat per grid point")
plt.show()
plt.plot(grid, logn, 'k')
plt.title("n vs ln(n)")
plt.xlabel("n")
plt.ylabel("ln(n)")
plt.show()