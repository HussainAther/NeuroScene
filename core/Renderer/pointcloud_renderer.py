import numpy as np
import moderngl
from pathlib import Path


class PointCloudRenderer:
    def __init__(self, ctx, point_data_path: str):
        self.ctx = ctx
        self.program = self._load_shader()

        self.positions = self._load_point_data(point_data_path)
        self.vbo = self.ctx.buffer(self.positions.astype('f4').tobytes())

        self.vao = self.ctx.vertex_array(
            self.program,
            [(self.vbo, '3f', 'in_position')]
        )

    def _load_shader(self):
        shader_dir = Path("core/Renderer/shaders")
        return self.ctx.program(
            vertex_shader=open(shader_dir / "points.vert").read(),
            fragment_shader=open(shader_dir / "points.frag").read()
        )

    def _load_point_data(self, path: str):
        if path.endswith('.csv'):
            return np.loadtxt(path, delimiter=",")
        elif path.endswith('.npy'):
            return np.load(path)
        else:
            raise ValueError(f"Unsupported point data format: {path}")

    def render(self, view, projection, time):
        self.program['view'].write(view.astype('f4'))
        self.program['projection'].write(projection.astype('f4'))
        self.program['time'].value = time

        self.ctx.enable(moderngl.POINT_SIZE)
        self.vao.render(mode=moderngl.POINTS)

