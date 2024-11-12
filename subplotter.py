# File: subplotter.py
import numpy as np
import matplotlib.pyplot as plt


# Generates subplots in horizontal order;
# takes in optional input to customize domain
def horiz_plots(domain_upper_limit = 2*np.pi):
    
    x = np.linspace(0, domain_upper_limit, 1000) # generates data from functions
    h = np.cos(x)
    k = np.sin(x)
    
    fig, ax = plt.subplots(1, 2, figsize = (12, 5)) # creates horizontal grid of subplots

    # plots each subplot with their respective titles and axes
    ax[0].plot(x,h)
    ax[0].set_ylabel("Y-Axis")
    ax[0].set_xlabel("X-Axis")
    ax[0].set_title("Graph of $cos(x)$")
    
    ax[1].plot(x,k)
    ax[1].set_ylabel("Y-Axis")
    ax[1].set_xlabel("X-Axis")
    ax[1].set_title("Graph of $sin(x)$")

    plt.show()


# Generates subplots in horizontal order;
# takes in optional input to customize domain
def vert_plots(domain_upper_limit = 2*np.pi):
    
    x = np.linspace(0, domain_upper_limit, 1000) # generates data from functions
    h = np.cos(x)
    k = np.sin(x)
    
    fig, ax = plt.subplots(2, 1, figsize = (5, 12)) # creates vertical grid of subplots

    # plots each subplot with their respective titles and axes
    ax[0].plot(x,h)
    ax[0].set_ylabel("Y-Axis")
    ax[0].set_xlabel("X-Axis")
    ax[0].set_title("Graph of $cos(x)$")
    
    ax[1].plot(x,k)
    ax[1].set_ylabel("Y-Axis")
    ax[1].set_xlabel("X-Axis")
    ax[1].set_title("Graph of $sin(x)$")

    plt.show()
    