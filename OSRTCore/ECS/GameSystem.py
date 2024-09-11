import EntityManager


class Behaviour:
    def update(self, entity_manger: EntityManger, delta_time):
        raise NotImplementedError("This method should be implemented by the subclass")

    def start(self, entity_manager):
        raise NotImplementedError("This method should be implemented by the subclass")
