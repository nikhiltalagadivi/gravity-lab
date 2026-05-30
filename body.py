import numpy as np

class Body:
    def __init__(self, pos, vel, mass, radius):
        self.pos = np.array(pos, dtype=float)
        self.vel = np.array(vel, dtype=float)
        self.mass = mass
        self.radius = radius

    def __repr__(self):
        return f"pos={self.pos}, vel={self.vel}, mass={self.mass}, radius={self.radius}"


