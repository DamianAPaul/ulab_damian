# File: polynomialplots.py
import numpy as np
import matplotlib.pyplot as plt


# generates 3x3 grid of subplots graphing 9 polynomial functions;
# takes in no inputs
def nine_polynomial_plots():

    x = np.linspace(-1, 1, 1000) # generates data from all 9 functions
    y2 = x**2
    y3 = x**3
    y4 = x**4
    y5 = x**5
    y6 = x**6
    y7 = x**7
    y8 = x**8
    y9 = x**9
    y10 = x**10

    fig, ax = plt.subplots(3, 3, figsize = (20, 20)) # creates 3x3 subplot grid

    ax[0, 0].plot(x, y2, label = "$x^{2}$") # plots every plot and with their labels
    ax[0, 1].plot(x, y3, label = "$x^{3}$")
    ax[0, 2].plot(x, y4, label = "$x^{4}$")
    ax[1, 0].plot(x, y5, label = "$x^{5}$")
    ax[1, 1].plot(x, y6, label = "$x^{6}$")
    ax[1, 2].plot(x, y7, label = "$x^{7}$")
    ax[2, 0].plot(x, y8, label = "$x^{8}$")
    ax[2, 1].plot(x, y9, label = "$x^{9}$")
    ax[2, 2].plot(x, y10, label = "$x^{10}$")
    
    for i, ax in enumerate(ax.flat): # gives every subplot axis and title labels and displays legends
        ax.set_xlabel("x")
        ax.set_ylabel("$f(x)$")
        ax.set_title(f"Graph of $x^{{{i+2}}}$", fontsize = 15)
        ax.legend()
        
        