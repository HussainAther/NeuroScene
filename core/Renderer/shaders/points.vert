#version 330 core

in vec3 in_position;

uniform mat4 view;
uniform mat4 projection;

void main() {
    gl_Position = projection * view * vec4(in_position, 1.0);
    gl_PointSize = 6.0;
}

