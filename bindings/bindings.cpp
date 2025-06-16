#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/stl_bind.h>
#include <pybind11/functional.h>

#include "core/SceneGraph/SceneNode.hpp"

namespace py = pybind11;

PYBIND11_MODULE(pyscene, m) {
    py::class_<SceneNode, std::shared_ptr<SceneNode>>(m, "SceneNode")
        .def(py::init<const std::string&>())
        .def_readwrite("name", &SceneNode::name)

        // Transform
        .def("set_local_transform", &SceneNode::setLocalTransform)
        .def("get_global_transform", &SceneNode::getGlobalTransform)

        // Metadata
        .def("set_metadata", &SceneNode::setMetadata)
        .def("get_metadata", &SceneNode::getMetadata,
             py::return_value_policy::reference_internal)

        // Hierarchy
        .def("add_child", &SceneNode::addChild)
        .def("get_children", &SceneNode::getChildren,
             py::return_value_policy::reference_internal);
}

