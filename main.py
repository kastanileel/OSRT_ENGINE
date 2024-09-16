# Engine Imports
from OSRTCore.ECS.EntityManager import EntityManager
from OSRTCore.ECS.GameSystem import GameSystems, ExampleSystem, game_system_registry

# Other Imports
import time
from itertools import product
import taichi as ti
import taichi.math as tm

from OSRTCore.raytracer.primitives import Triangle
from OSRTCore.raytracer.rtBasics import Ray
from OSRTCore.utils.WavefrontOBJParser import WavefrontOBJParser
from OSRTCore.utils.Window import Window

ti.init(arch=ti.gpu)
gameSystems = GameSystems()
manager = EntityManager()
window = Window("OSRT_ENGINE v0.1", 640, 480)
image = ti.Vector.field(3, ti.f32, shape=(640, 480))
parsed_obj = WavefrontOBJParser.parse("./assets/teapot.obj")
num_triangles = 6320
mesh = Triangle.field(shape=num_triangles)


def initEngine():
    # Initialize the engine
    for system in game_system_registry:
        gameSystems.addSystem(system())

    for i in range(num_triangles):
        mesh[i] = parsed_obj[i]

    pass


@ti.func
def complex_sqr(z):  # complex square of a 2D vector
    return tm.vec2(z[0] * z[0] - z[1] * z[1], 2 * z[0] * z[1])


@ti.kernel
def test_kernel(t: float):
    for i, j in image:  # Parallelized over all pixels
        c = tm.vec2(-0.8, tm.cos(t) * 0.2)
        z = tm.vec2(i / 640 - 1, j / 480 - 0.5) * 2
        iterations = 0
        while z.norm() < 20 and iterations < 50:
            z = complex_sqr(z) + c
            iterations += 1
        image[i, j] = 1 - iterations * 0.02


@ti.kernel
def test_kernel2(t: float):
    for i, j in image:
        u = i / 640
        v = j / 480
        u = u * 2.0 - 1.0
        v = v * 2.0 - 1.0
        u *= 20
        v *= 20
        ray = Ray()
        ray.origin = tm.vec3(u, v, -20)
        ray.direction = tm.vec3(0, 0, 1)
        image[i, j] = 0.0
        for triangle in range(num_triangles):
            did_hit, ta = mesh[triangle].intersect(ray)
            if did_hit:
                image[i, j] = 1.0



if __name__ == "__main__":

    initEngine()
    # Initialize the engine
    system_time_last = time.time_ns()
    # Game Loop
    count = 0

    while True:
        delta_time = (time.time_ns() - system_time_last) / 1e9
        system_time_last = time.time_ns()

        gameSystems.update(manager, delta_time)
        test_kernel2(count * 0.03)
        window.buffer = image
        window.update()
        count += 1
    pass
