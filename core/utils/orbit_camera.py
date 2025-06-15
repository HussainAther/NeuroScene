# core/utils/orbit_camera.py
import numpy as np
from pyrr import Matrix44, Vector3


class OrbitCamera:
    def __init__(self, radius=5.0, target=(0.0, 0.0, 0.0)):
        self.radius = radius
        self.theta = np.pi / 2  # horizontal angle
        self.phi = np.pi / 4    # vertical angle
        self.target = Vector3(target)

    def rotate(self, d_theta, d_phi):
        self.theta += d_theta
        self.phi = np.clip(self.phi + d_phi, 0.01, np.pi - 0.01)

    def zoom(self, delta):
        self.radius = max(0.1, self.radius + delta)

    def get_view_matrix(self):
        x = self.radius * np.sin(self.phi) * np.cos(self.theta)
        y = self.radius * np.cos(self.phi)
        z = self.radius * np.sin(self.phi) * np.sin(self.theta)
        eye = Vector3([x, y, z]) + self.target
        return Matrix44.look_at(eye, self.target, (0.0, 1.0, 0.0))

