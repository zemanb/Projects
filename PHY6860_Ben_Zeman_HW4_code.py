from numpy import *
import matplotlib.pyplot as plt
n_grid = []     # will use these arrays to model grid density and iteration steps
n_iter = []     # commented out program is for earler steps, final program is for part D
for L in [3, 6, 9, 12, 15]: # variation of number of grid points each direction
# L = 10
    dv = 0
    r_boundary = 5

    v_old = zeros((L + 2, L + 2)) # 2d arrays updated in loops
    v_new = zeros((L + 1, L + 1))
    charge_density = zeros((L + 1, L + 1))
    xmin = -L/2   #converts indeces to grid points
    ymin = -L/2
    dx = (ymin-xmin) / L
    dy = dx
    n = 0
    e = [] #used for error vs iteration steps


    def i(x):
        return int((x - xmin) / dx + .5)  #grid points to indeces


    def j(y):
        return int((y - ymin) / dy + .5)


    charge_density[i(0.6), j(0)] = 1   # creating charge density grid for the dipole
    charge_density[i(-0.6), j(0)] = 1



    error = 1E-5
# for error in [1E-5, 5E-6, 1E-6, 5E-7]:  # for part B, error tolerance vs iterations
    while dv > error or dv == 0:   # controls number of iterations

        dv = 0  # initializes change in potential
        dv0 = 0  # used for accuracy of solution, compares to last iterations

        for j in range(L):    #complete grid iteration
            for i in range(L):
                x = xmin + (i * dx)  # index to grid conversion
                y = ymin + (j * dy)
                if x ** 2 + y ** 2 < r_boundary ** 2:   #boundary condition
                    v_new[i, j] = .25 * (v_old[i + 1, j] + v_old[i - 1, j] + v_old[i, j + 1] + v_old[i, j - 1] + charge_density[j, i]) #changing potential grid
                    if v_old[i, j] != 0: #prevents divide by 0 error
                        dv = (v_new[i, j]-v_old[i, j])/v_old[i, j]  #accuracy of soln method
                        if dv <= dv0:
                            dv = dv0
                # if x ** 2 + y ** 2 < r_boundary ** 2:    # tolerance method
                #     dv += abs(v_new[i, j] - v_old[i, j])
                # else:
                #     dv = dv
        for j in range(L):
            for i in range(L):
                v_old[i, j] = v_new[i, j] #allows for future grid updates

        n += 1   #used to count iteration steps
    N = n
    n_iter.append(N)
    n_grid.append(L)   # number of grid points each direction
    # e.append(error)
# x_grid = linspace(-5, 5, L+1)  #axes for contour
# y_grid = linspace(-5, 5, L+1)
# cs = plt.contour(x_grid, y_grid, v_new)    #contour plot with equipotentials
# plt.clabel(cs)
# plt.xlabel("x coordinate")
# plt.ylabel("y coordinate")
# plt.title("Equipotential lines of a dipole (Volts)")
# plt.plot(n_iter, e, 'b*')               # iterations vs error threshold
# plt.yticks((1E-5, 5E-6, 1E-6, 5E-7), ['1E-5', '5E-6', '1E-6', '5E-7'] )
# plt.xlabel("number of iterations")
# plt.ylabel("error tolerance (volts)")
# plt.title("Number of potential grid updates vs change of potential threshold")
# plt.plot(n_grid, n_iter, 'r^', label="Jacobi")    # iterations vs grid density, on same graph as for SOR method
# plt.title("Potential grid updates vs grid density")
plt.plot(n_grid, n_iter, 'k^', label="Jacobi")     # iterations vs grid density but for accuracy of soln method
plt.title("Potential grid updates vs grid density (Accuracy of solution method")
plt.ylabel("number of iterations")
plt.xlabel("number of grid points each dimension")
# plt.show()

n_grid = []  # this half of the program is similar to the first part, but doesn't have a contour plot or variation of error tolerance
n_iter = []  # uses SOR method instead of Jacobi, the changes I will describe below
for L in [10, 20, 30, 40, 50]:  # used different densities to allow the graph to accurately display the two relationships
# L = 10                        # for Jacobi and SOR
    dv = 0
    r_boundary = 5

    v_old = zeros((L + 2, L + 2))
    v_new = zeros((L + 1, L + 1))
    v_star = zeros((L, L))
    charge_density = zeros((L + 1, L + 1))
    xmin = -L/2
    ymin = -L/2
    dx = (ymin-xmin) / L
    dy = dx
    n = 0
    e = []


    def i(x):
        return int((x - xmin) / dx + .5)


    def j(y):
        return int((y - ymin) / dy + .5)


    charge_density[i(0.6), j(0)] = 1
    charge_density[i(-0.6), j(0)] = 1



    error = 1E-5

    while dv > error or dv == 0:
        dv = 0
        dv0 = 0
        for j in range(L):
            for i in range(L):
                x = xmin + (i * dx)
                y = ymin + (j * dy)
                if x ** 2 + y ** 2 < r_boundary ** 2:
                    v_star[i, j] = .25 * (v_old[i + 1, j] + v_new[i - 1, j] + v_old[i, j + 1] + v_new[i, j - 1] + charge_density[i, j])# SOR method uses values from the current grid iteration to update points on the grid
                    alpha = 2 / (1 + pi/L)   #this value affects the rate in which the change of potential approaches error tolerance
                    dv_per_step = v_star[i, j] - v_old[i, j] # uses change of potential during one iteration
                    # dv += v_star[i, j] - v_old[i, j]   # for error tolerance method
                    v_new[i, j] = alpha*dv_per_step + v_old[i, j]  # change of potential during one iteration affects the potential after the iteration
                    if v_old[i, j] != 0:     #accuracy of solns method
                        dv = abs((v_new[i, j]-v_old[i, j])/v_old[i, j])
                        if dv <= dv0:
                            dv = dv0
        for j in range(L):
            for i in range(L):
                v_old[i, j] = v_new[i, j]

        n += 1
    N = n
    n_iter.append(N)
    n_grid.append(L)

plt.plot(n_grid, n_iter, 'go', label="SOR")  #only the grid density vs iterations plots, for error tolerance and accuracy of solns, are graphed
plt.ylabel("number of iterations")
plt.xlabel("number of grid points each dimension")
# plt.title("Potential grid updates vs grid density")
plt.title("Potential grid updates vs grid density (Accuracy of Solution)")
plt.legend()
plt.show()




