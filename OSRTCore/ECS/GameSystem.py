from OSRTCore.ECS.EntityManager import EntityManager

# Global registry for game systems
game_system_registry = []
class BehaviourMeta(type):
    def __init__(cls, name, bases, clsdict):
        super().__init__(name, bases, clsdict)

        if cls.__name__ != "GameSystems" and cls.__name__ != "Behaviour":
            game_system_registry.append(cls)


class Behaviour(metaclass=BehaviourMeta):
    def update(self, entity_manger: EntityManager, delta_time):
        raise NotImplementedError("This method should be implemented by the subclass")

    def start(self, entity_manager):
        raise NotImplementedError("This method should be implemented by the subclass")


class GameSystems(Behaviour):
    """ Composite of all the systems in the game
    """
    instance = None

    def __init__(self):
        self.systems = []

    def addSystem(self, system):
        self.systems.append(system)

    def update(self, entity_manager: EntityManager, delta_time):
        for system in self.systems:
            system.update(entity_manager, delta_time)

    def start(self, entity_manager):
        for system in self.systems:
            system.start(entity_manager)


class ExampleSystem(Behaviour):
    def update(self, entity_manager, delta_time):
        print("Example System updating." + str(delta_time))
        pass

    def start(self, entity_manager):
        print("Example System starting.")
        pass

