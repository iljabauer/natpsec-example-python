from persistence import entities
class InMemoryPersistenceContext(object):
    """The InMemoryPersistenceContext is a very basic store for entity
     objects. It basically holds all objects in memory. In a real application,
     this will probably be replaced by a Data Access Object (DAO) that retrieves
     object from and stores objects to a database."""

    # This fields holds the single instance of this class.
    __instance = None
    
    class __impl(object):
        def __init__(self):
            self.flights = {}
            self.airplanes = {}
            self.passengers = {}
        
        def update(self, entity):
            """Stores the given entity.
            :param entity: the entity to store
            """
            update_dict = {entity.id: entity}
            if isinstance(entity, entities.Flight):
                self.flights.update(update_dict)
                return
            if isinstance(entity, entities.AirplaneType):
                self.airplanes.update(update_dict)
                return
            if isinstance(entity, entities.Passenger):
                self.passengers.update(update_dict)
                return
        
        def create_flight(self, name):
            """Creates a new flight with the given name.
            :param name: the name of the flight.
            :returns: the created object
            """
            flight = entities.Flight(name)
            self.update(flight)
            return flight
            
        def create_passenger(self, first_name, last_name):
            """Creates a new passenger with the given first and last name.
            :param first_name: the first name of the passenger.
            :param last_name: the name of the passenger.
            :returns: the created object
            """
            passenger = entities.Passenger(first_name, last_name)
            self.update(passenger)
            return passenger
            
        
        def create_airplane_type(self, name):
            """Creates a new type of airplane with the given name.
            :param name: the name of the airplane type.
            :returns: the created object.
            """
            airplane_type = entities.AirplaneType(name)
            self.update(airplane_type)
            return airplane_type
        
        
    def __init__(self):
        """Creates the one and only instance of this class."""
        
        if InMemoryPersistenceContext.__instance is None:
            InMemoryPersistenceContext.__instance = InMemoryPersistenceContext.__impl()
        self.__dict__['_InMemoryPersistenceContext__instance'] = InMemoryPersistenceContext.__instance
        
    def __getattr__(self, attr):
        """Delegate access to implementation"""
        return getattr(self.__instance, attr)

    def __setattr__(self, attr, value):
        """Delegate access to implementation"""
        return setattr(self.__instance, attr, value)
