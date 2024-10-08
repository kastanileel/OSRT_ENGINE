class EntityManager:

    """ Basically an 'Entity' is just a collection of components represented by an id.

    However, Entities should have children and parents, therefore we need to keep track of the mapping
    of the entities and their relationships.
    """
    entityRelationGraph = {}

    def subscribeComponent(self, componentType)->int:
        """This method is called before initializing the entity manager.
        Each component type should be registered to enable the mapping of component type to flag.

        :param componentType: the type of the component
        :return: the flag of the entity type
        """
        pass


    def createEntity(self, flag:int)->int:
        """
        :flag: flag stands for all components that the entity has
        :return: the entity id
        """
        pass

    def destroyEntity(self, entityId:int):
        """
        :entityId: the entity id
        """
        pass

    def __clearDestroyedEntities(self):
        pass
