from pyscene import SceneNode
from pyrr import Matrix44


def print_scene(node, indent=0):
    print("  " * indent + f"{node.name} [{node.get_metadata().get('type', 'Node')}]")
    for key, value in node.get_metadata().items():
        if key != "type":
            print("  " * (indent + 1) + f"{key}: {value}")
    for child in node.get_children():
        print_scene(child, indent + 1)


def test_basic_scene():
    # Create root
    root = SceneNode("Root")
    root.set_metadata("type", "Group")

    # Add a brain mesh
    cortex = SceneNode("CortexMesh")
    cortex.set_metadata("type", "Mesh")
    cortex.set_metadata("geometry", "assets/brain.obj")
    cortex.set_metadata("material", "materials/brain_shader.json")
    cortex.set_local_transform(Matrix44.from_translation([0, 0, 0]))

    # Add a neuron point cloud
    neurons = SceneNode("NeuronSpikes")
    neurons.set_metadata("type", "PointCloud")
    neurons.set_metadata("data", "data/spikes.csv")

    # Add a camera node
    camera = SceneNode("CameraRig")
    camera.set_metadata("type", "Camera")
    camera.set_metadata("fov", "45")
    camera.set_metadata("orbit", "radius=3.5, theta=1.5, phi=0.8")

    # Build hierarchy
    root.add_child(cortex)
    root.add_child(neurons)
    root.add_child(camera)

    # Print hierarchy
    print_scene(root)


if __name__ == "__main__":
    test_basic_scene()

