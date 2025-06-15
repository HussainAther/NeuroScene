#version 330 core

in vec2 frag_uv;
in vec3 frag_pos;

uniform sampler2D activity_map;  // EEG heatmap
uniform float time;

out vec4 fragColor;

void main() {
    float activity = texture(activity_map, frag_uv).r;

    // Color-mapped brain signal with animated glow
    float r = sin(activity * 10.0 + time * 0.5) * 0.5 + 0.5;
    float g = sin(activity * 10.0 + time * 0.7 + 1.0) * 0.5 + 0.5;
    float b = sin(activity * 10.0 + time * 0.9 + 2.0) * 0.5 + 0.5;

    float glow = smoothstep(0.1, 1.0, activity);
    fragColor = vec4(r * glow, g * glow, b * glow, 1.0);
}

