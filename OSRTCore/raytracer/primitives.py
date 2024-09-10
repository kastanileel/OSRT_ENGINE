import taichi as ti
import taichi.math as tm


class Primitive:
    @ti.func
    def intersect(self, ray):
        raise NotImplementedError


@ti.dataclass
class Triangle(Primitive):
    v0: tm.vec3
    v1: tm.vec3
    v2: tm.vec3

    @ti.func
    def intersect(self, ray):
        pass


@ti.dataclass
class Sphere(Primitive):
    origin: tm.vec3
    radius: ti.f32

    @ti.func
    def intersect(self, ray):
        pass
