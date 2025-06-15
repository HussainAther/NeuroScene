import moderngl
import numpy as np
import pygame
from pygame import display
from pyrr import Matrix44

WIDTH, HEIGHT = 800, 600

# Sample EEG mock data
brain_activity = np.random.rand(100, 100)

ctx = moderngl.create_context()
prog = ctx.program(
    vertex_shader="""
        #version 330
        in vec2 in_position;
        void main() {
            gl_Position = vec4(in_position, 0.0, 1.0);
        }
    """,
    fragment_shader="""
        #version 330
        out vec4 fragColor;
        uniform float time;
        void main() {
            fragColor = vec4(sin(time), 0.2, 0.8, 1.0);
        }
    """,
)

vertices = np.array([
    -1.0, -1.0,
     1.0, -1.0,
    -1.0,  1.0,
     1.0,  1.0,
], dtype='f4')

vbo = ctx.buffer(vertices.tobytes())
vao = ctx.simple_vertex_array(prog, vbo, 'in_position')

pygame.init()
screen = display.set_mode((WIDTH, HEIGHT), pygame.OPENGL | pygame.DOUBLEBUF)

clock = pygame.time.Clock()
running = True
t = 0.0

while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    t += 0.016
    ctx.clear(0.0, 0.0, 0.0)
    prog['time'].value = t
    vao.render(moderngl.TRIANGLE_STRIP)
    display.flip()
    clock.tick(60)

