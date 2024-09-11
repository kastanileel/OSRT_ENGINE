# Engine Imports
from OSRTCore.ECS.EntityManager import EntityManager
from OSRTCore.ECS.GameSystem import GameSystems, ExampleSystem, game_system_registry

# Other Imports
import time
gameSystems = GameSystems()
manager = EntityManager()


def initEngine():
    # Initialize the engine
    for system in game_system_registry:
        gameSystems.addSystem(system())

    pass


if __name__ == "__main__":
    initEngine()
    # Initialize the engine
    system_time_last = time.time_ns()
    # Main loop:
    while True:

        delta_time = (time.time_ns() - system_time_last) / 1e9
        system_time_last = time.time_ns()

        gameSystems.update(manager, delta_time)
    pass
