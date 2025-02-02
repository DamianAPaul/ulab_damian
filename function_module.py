#function_module.py

# Orbital Period function
def orbital_period(a):
    # with semi-major axis input a, calculates the orbital period by Kepler's Third Law
    period = (a**3)**0.5
    return period