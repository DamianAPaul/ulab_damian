# File: my_module.py

import numpy as np


def time_change(times):
    """
    Goes through multiple time sets and calculates the net time change (subtracting the last time value by
    the first time value).
    Input: multidimensional array of multiple time steps
    Output: 1-D np.array of time difference 
    """
    
    first_values = [] # initializes empty lists to return final values
    last_values = []
    for x in times: # goes through each time set, adds first time value
        first_values.append(x[0]) 
    for x in times:
        last_values.append(x[len(x) - 1])

    first_values = np.array(first_values) # converts each list into an array for operations
    last_values = np.array(last_values)
    time_changes = last_values - first_values # subtracts arrays to find net time changes

    return time_changes



def highest_time_value(times):
    """
    Calculates the highest time value (maximum number) in any multi-dimensional array of time sets with 
    time values.
    Input: multidimensional array of multiple time steps
    Output: single integer that is the maximum time value from all time sets
    """

    maximum_value = 0
    for x in times: # goes through each set
        for i in range(len(x)): # goes through each value in set
            if x[i] > maximum_value: # sets maximum_value equal to highest number in all sets
                maximum_value = x[i]

    return maximum_value



def shortest_time_change(times):
    """
    Finds the lowest-number time change in array of all time changes.
    Input: 1-D array of time changes
    Output: single integer that is the smallest time change value from time sets
    """

    time_changes = time_change(times) # uses previous function to calculate time changes
    for x in time_changes: # goes through each value in time_changes array
        if x < highest_time_value(times): # sets minimum_value equal to lowest number in array
            minimum_value = x

    return minimum_value

