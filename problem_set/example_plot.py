# load the necessary libraries
import matplotlib.pyplot as plt
import numpy as np


# theory plot
x_values = np.linspace(1,20,10)  			# produce 10 equally spaced points between 1 and 20
y_values = x_values**2  				# square each element in the vector
plt.figure(1) 								# First plot is figure1
plt.plot(x_values, y_values) 				# Plot theory data, line connects points


# data plot
experimentinput = np.loadtxt("data.txt", delimiter=",")	# load input data from file, comma separated
experiment = np.transpose(experimentinput)	# transpose so x, y, y-error are separate row vectors
x_data = experiment[0]					# for clarity, explicitly name vectors
y_data = experiment[1]
y_error = experiment[2]
plt.figure(2)								# next plot is figure2
plt.errorbar(x_data, y_data, yerr=y_error, fmt='kx')  # scatter plot with error bars, 'kx'=plot as black x
#plot(x_data, y_data,'k.')  			# plots without error bars, 'k.' plots as black points


# example of combining theory and data plot
plt.figure(3)
plt.plot(x_values, y_values) 				# plot theory
plt.errorbar(x_data, y_data, yerr=y_error, fmt='ro')  # on top, also plot experiment, 'ro'=plot as red o
plt.xlabel("Kittens")						# Always label your plots!
plt.ylabel("Pirates")
plt.title("Pirates vs Kittens")
plt.semilogx()								# now plot x on log axis
# xlim([0.5, 25])						# manual definition of x axis limits [xmin, xmax]
# ylim([-20, 450])						# manual definition of y axis limits [ymin, ymax]
plt.show()									# display figures(), always do last

# These are the commands to make a log plot in y or both
# semilogy()
# loglog()
