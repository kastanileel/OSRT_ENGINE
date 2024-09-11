import taichi as ti
import taichi.math as tm


class Component:
    pass


class Transform(Component):
    position: tm.vec3
    rotation: tm.vec3
    scale: tm.vec3


class Renderer(Component):
    pass
