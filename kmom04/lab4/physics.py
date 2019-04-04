"""
Physics calculations
"""
def free_fall(time, initial_speed=0, gravity=9.82):
    """
    Returns the free fall speed
    """
    speed = initial_speed + gravity * time
    return speed

def kinetic_energy(mass, time, in_speed, gravity):
    """
    Returns the kinetic energy
    """
    v = free_fall(time, in_speed, gravity)
    energy = 0.5 * mass * pow(v, 2)
    return energy

def height(mass, time, in_speed, gravity):
    """
    Returns the calculated height causing the given energy
    """

    fall_height = kinetic_energy(mass, time, in_speed, gravity) / (mass * gravity)
    return fall_height

def gravitational_pull(m1, m2, r):
    """
    Returns the calculated force from the pull between two objects
    """

    G = 6.674 * pow(10, -11)
    force = G * m1 * m2 / pow(r, 2)
    return force
