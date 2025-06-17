import pygame
from pygame import display
import moderngl
from core.SceneGraph.scene_runtime import SceneRuntime

WIDTH, HEIGHT = 800, 600

pygame.init()
screen = display.set_mode((WIDTH, HEIGHT), pygame.OPENGL | pygame.DOUBLEBUF)
ctx = moderngl.create_context()
clock = pygame.time.Clock()

scene = SceneRuntime(ctx, "examples/neuron_scene.json", WIDTH, HEIGHT)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    delta = clock.tick(60) / 1000.0
    scene.render(delta)
    display.flip()

