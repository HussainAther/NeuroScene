#version 330 core

// Input attributes from mesh
in vec3 in_position;
in vec2 in_uv;

// Uniforms (set from Python)
uniform mat4 model;
uniform mat4 view;
uniform mat4 projection;

// Outputs to fragment shader
out vec2 frag_uv;
out vec3 frag_pos;

void main() {
    frag_uv = in_uv;
    frag_pos = vec3(model * vec4(in_position, 1.0));
    gl_Position = projection * view * vec4(frag_pos, 1.0);
}

