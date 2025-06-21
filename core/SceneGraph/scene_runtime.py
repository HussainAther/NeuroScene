from core.Renderer.renderer import BrainRenderer
from core.SceneGraph.scene_loader import load_scene
from core.utils.orbit_camera import OrbitCamera
from core.Renderer.pointcloud_renderer import PointCloudRenderer

import numpy as np


class SceneRuntime:
    def __init__(self, ctx, json_path, width=800, height=600):
        self.ctx = ctx
        self.width = width
        self.height = height
        self.scene_root = load_scene(json_path)
        self.camera = OrbitCamera()

        self.renderer = BrainRenderer(ctx, width, height)
        self._configure_camera()

    def _configure_camera(self):
        # Search scene for camera node
        for node in self.scene_root.get_children():
            if node.get_metadata().get("type") == "Camera":
                orbit = node.get_metadata().get("orbit")
                if orbit:
                    # Parse "radius=3.5, theta=1.5, phi=0.8"
                    parts = dict(p.split("=") for p in orbit.split(", "))
                    self.camera.radius = float(parts["radius"])
                    self.camera.theta = float(parts["theta"])
                    self.camera.phi = float(parts["phi"])

    def _dispatch_renderables(self):
        self.renderables = []

        for node in self.scene_root.get_children():
            if node.get_metadata().get("type") == "PointCloud":
                path = node.get_metadata().get("data", "")
                renderer = PointCloudRenderer(self.ctx, path)
                self.renderables.append(renderer)

    def render(self, dt):
        self.renderer.camera = self.camera
        self.renderer.render(dt)
        for r in self.renderables:
            r.render(view, projection, self.time)

