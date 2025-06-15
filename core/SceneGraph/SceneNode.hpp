#pragma once

#include <string>
#include <vector>
#include <memory>
#include <glm/glm.hpp>
#include <glm/gtc/matrix_transform.hpp>

class SceneNode {
public:
    std::string name;
    glm::mat4 localTransform = glm::mat4(1.0f);
    std::weak_ptr<SceneNode> parent;
    std::vector<std::shared_ptr<SceneNode>> children;

    SceneNode(const std::string& name_) : name(name_) {}

    void setParent(std::shared_ptr<SceneNode> newParent) {
        parent = newParent;
        newParent->children.push_back(shared_from_this());
    }

    void setLocalTransform(const glm::mat4& transform) {
        localTransform = transform;
    }

    glm::mat4 getGlobalTransform() const {
        if (auto p = parent.lock()) {
            return p->getGlobalTransform() * localTransform;
        }
        return localTransform;
    }
};

