import numpy as np


# Gravitational constant
G = 1

# newton's universal law of gravitation to compute forces between two objects
def compute_force(body1, body2):
    vector_r = body2.pos - body1.pos
    distance_r = np.linalg.norm(vector_r)

    # to prevent infinite force error
    if distance_r == 0:
        return np.array([0.0, 0.0])

    # magnitude of the force between two bodies
    force_mag = G * body1.mass * body2.mass / (distance_r ** 2)

    # unit vector to determine direction
    force_dir = vector_r / distance_r

    # return the vector force
    return force_mag * force_dir

# standard kinematic equation for updating position
def update_body(body, total_force, dt):
    acceleration = total_force / body.mass

    body.vel += acceleration * dt

    body.pos += body.vel * dt

