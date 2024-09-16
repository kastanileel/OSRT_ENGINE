import taichi as ti

from OSRTCore.ECS.EntityManager import EntityManager
from OSRTCore.ECS.GameSystem import Behaviour


class Window:

    def __init__(self, title, width, height):
        self.bufferUpdated = False
        self.title = title
        self.buffer = ti.Vector.field(3, ti.f32, shape=(width, height))
        self.gui = ti.GUI(self.title, (width, height), fast_gui=True)
        self.gui.set_image(self.buffer)

    def update(self):
        # create a thread to run the window
        self.gui.set_image(self.buffer)
        self.gui.show()
