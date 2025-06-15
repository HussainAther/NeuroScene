import json
from pathlib import Path
from pyscene import SceneNode  # From your pybind11 bindings

def load_transform(data):
    # Fallbacks
    translate = data.get("translate", [0, 0, 0])
    rotate = data.get("rotate", [0, 0, 0])
    scale = data.get("scale", [1, 1, 1])

    # Convert to a 4x4 matrix (simplified, replace with proper rotation if needed)
    from pyrr import Matrix44, Vector3
    transform = Matrix44.identity()
    transform *= Matrix44.from_scale(Vector3(scale))
    transform *= Matrix44.from_translation(Vector3(translate))
    return transform

def build_node(data, parent=None):
    node = SceneNode(data["name"])
    transform = load_transform(data.get("transform", {}))
    node.set_local_transform(transform)

    if parent:
        parent.add_child(node)

    # Optionally attach metadata for geometry, material, etc.
    # Could be stored in a dictionary or attributes in the C++ side later

    for child in data.get("children", []):
        build_node(child, node)

    return node

def load_scene(filepath: str):
    with open(filepath) as f:
        scene_json = json.load(f)

    root_node = None
    for top_level in scene_json["scene"]["nodes"]:
        root_node = build_node(top_level)

    return root_node

