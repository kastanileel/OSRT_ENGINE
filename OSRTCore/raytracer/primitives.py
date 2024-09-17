import taichi as ti
import taichi.math as tm

""""
BVH STUFF:
    - AABB 
"""


@ti.dataclass
class AABB:
    intervals: ti.field(ti.f32, shape=(3, 2))

    def __int__(self, p0: tm.vec3, p1: tm.vec3):
        self.intervals[0, 0] = tm.min(p0.x, p1.x)
        self.intervals[1, 0] = tm.min(p0.y, p1.y)
        self.intervals[2, 0] = tm.min(p0.z, p1.z)

        self.intervals[0, 1] = tm.max(p0.x, p1.x)
        self.intervals[1, 1] = tm.max(p0.y, p1.y)
        self.intervals[2, 1] = tm.max(p0.z, p1.z)

    @ti.func
    def intersect(self, ray):
        # TODO: Add tmin and tmax to ray
        t_min = -10000.0
        t_max = 10000.0
        for dimension in range(3):
            inv = 1.0 / ray.direction[dimension]

            t0 = (self.intervals[dimension, 0] - ray.direction[dimension]) * inv
            t1 = (self.intervals[dimension, 1] - ray.direction[dimension]) * inv

            if t0 < t1:
                if t0 > t_min:
                    t_min = t0
                if t1 < t_max:
                    t_max = t1
            else:
                if t1 > t_min:
                    t_min = t1
                if t0 < t_max:
                    t_max = t0

            if t_max <= t_min:
                return False
        return True


class Primitive:
    @ti.func
    def intersect(self, ray):
        raise NotImplementedError

    @ti.func
    def bounding_box(self):
        raise NotImplementedError


@ti.dataclass
class BVHNode(Primitive):
    aabb: AABB

    @ti.func
    def intersect(self, ray):
        pass

    @ti.func
    def bounding_box(self):
        pass


@ti.dataclass
class Triangle(Primitive):
    v0: tm.vec3
    v1: tm.vec3
    v2: tm.vec3

    def __init__(self, v0, v1, v2):
        self.v0 = v0
        self.v1 = v1
        self.v2 = v2

    @ti.func
    def intersect(self, ray):
        """Moeller-Trumbore intersection

        No precomputation of the plane equation containing the triangle needed

        :param ray:
        :return: did_intersect boolean, hitrecord
        """
        did_hit = True
        edge1 = self.v1 - self.v0
        edge2 = self.v2 - self.v0
        ray_cross_edge2 = tm.cross(ray.direction, edge2)
        det = tm.dot(edge1, ray_cross_edge2)

        if det == 0.0:
            did_hit = False

        inv_det = 1.0 / det
        s = ray.origin - self.v0
        u = inv_det * tm.dot(s, ray_cross_edge2)
        if u < 0.0 or u > 1.0:
            did_hit = False

        s_cross_edge1 = tm.cross(s, edge1)
        v = inv_det * tm.dot(ray.direction, s_cross_edge1)
        if v < 0.0 or v > 1.0:
            did_hit = False

        t = inv_det * tm.dot(edge2, s_cross_edge1)

        if t <= 0.0:
            did_hit = False

        return did_hit, t


@ti.dataclass
class Sphere(Primitive):
    origin: tm.vec3
    radius: ti.f32

    @ti.func
    def intersect(self, ray):
        pass
