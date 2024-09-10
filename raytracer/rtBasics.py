import taichi as ti
import taichi.math as tm

@ti.dataclass
class Ray:
    origin: tm.vec3
    direction: tm.vec3

    def at(self, t):
        return self.origin + self.direction * t

@ti.dataclass
class HitRecord:
    p: tm.vec3
    normal: tm.vec3


class Material:
    @ti.func
    def scatter(self, ray_in, hit_record):
        pass