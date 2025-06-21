#version 330 core

uniform float time;

out vec4 fragColor;

void main() {
    float pulse = sin(time * 3.0 + gl_FragCoord.x * 0.05) * 0.5 + 0.5;
    fragColor = vec4(pulse, 0.8 * pulse, 1.0, 1.0);
}

