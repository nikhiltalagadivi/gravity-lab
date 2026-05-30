import pygame
import sys
import numpy as np
from body import Body
from physics import compute_force, update_body


pygame.init()
WIDTH, HEIGHT = 1920, 1080

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

sun = Body(pos=[400, 300], vel=[0, 0], mass=200000, radius=30)
earth = Body(pos=[200, 300], vel=[0, 40], mass=100000, radius=20)
planet_x = Body(pos=[300, 100], vel=[45, 0], mass=1, radius=10)

sun.colour = (255, 215, 0)
earth.colour = (100, 149, 237)
planet_x.colour = (130, 121, 198)

bodies = [sun, earth, planet_x]

dt = 0.1

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # debug
    # print(f"Earth position: {earth.pos}")

    # physics logic
    for b1 in bodies:
        total_force = np.array([0.0, 0.0])
        for b2 in bodies:
            force = compute_force(b1, b2)
            total_force += force

        update_body(b1, total_force, dt)

    # rendering
    screen.fill((0, 0, 0))

    # draw bodies
    for b in bodies:
        draw_pos = b.pos.astype(int).tolist()
        pygame.draw.circle(screen, b.colour, draw_pos, b.radius)


    # refresh
    pygame.display.flip()

    #fps
    clock.tick(120)