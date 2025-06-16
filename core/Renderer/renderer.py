import moderngl
import numpy as np
from pathlib import Path
from pyrr import Matrix44
from core.utils.orbit_camera import OrbitCamera

class BrainRenderer:
    def __init__(self, ctx, width=800, height=600):
        self.ctx = ctx
        self.width = width
        self.height = height
        self.time = 0.0

        # Load shaders
        shader_dir = Path("core/Renderer/shaders")
        self.prog = ctx.program(
            vertex_shader=open(shader_dir / "brain.vert").read(),
            fragment_shader=open(shader_dir / "brain.frag").read(),
        )

        # Example quad (replace this with your actual brain mesh VBO/VAO)
        vertices = np.array([
            -1.0, -1.0, 0.0,   0.0, 0.0,
             1.0, -1.0, 0.0,   1.0, 0.0,
            -1.0,  1.0, 0.0,   0.0, 1.0,
             1.0,  1.0, 0.0,   1.0, 1.0,
        ], dtype='f4')

        self.vbo = ctx.buffer(vertices.tobytes())
        self.vao = ctx.vertex_array(
            self.prog,
            [
                (self.vbo, '3f 2f', 'in_position', 'in_uv'),
            ]
        )

        # Camera
        self.camera = OrbitCamera(radius=3.0)

        # Fake EEG heatmap (100x100 grayscale)
        self.eeg_data = np.random.rand(100, 100).astype('f4')
        self.eeg_texture = ctx.texture(self.eeg_data.shape, 1, (self.eeg_data * 255).astype('u1').tobytes())
        self.eeg_texture.build_mipmaps()
        self.eeg_texture.use(location=0)

    def render(self, delta_time):
        self.time += delta_time

        self.ctx.clear(0.05, 0.05, 0.1)
        self.ctx.enable(moderngl.DEPTH_TEST)

        model = Matrix44.identity(dtype='f4')
        view = self.camera.get_view_matrix().astype('f4')
        projection = Matrix44.perspective_projection(45.0, self.width / self.height, 0.1, 100.0).astype('f4')

        self.prog['model'].write(model)
        self.prog['view'].write(view)
        self.prog['projection'].write(projection)
        self.prog['time'].value = self.time
        self.prog['activity_map'].value = 0

        self.vao.render(moderngl.TRIANGLE_STRIP)

