#pragma once

#include <string>
#include <vector>
#include <memory>
#include <unordered_map>
#include <glm/glm.hpp>

class SceneNode {
public:
    std::string name;
    glm::mat4 transform;
    std::vector<std::shared_ptr<SceneNode>> children;

    SceneNode(const std::string& name_) : name(name_), transform(glm::mat4(1.0f)) {}

    void addChild(std::shared_ptr<SceneNode> child) {
        children.push_back(child);
    }

    void setTransform(const glm::mat4& t) {
        transform = t;
    }

    glm::mat4 getGlobalTransform() const {
        // Placeholder for hierarchical transform accumulation
        return transform;
    }
};

