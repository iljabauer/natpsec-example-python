class Entity(object):
    # A global counter that holds the next available entity ID.
    _counter = 0
    
    def __init__(self):
        """Creates a new entity and initialized its ID."""
        Entity._counter += 1
        self.id = Entity._counter
        
    
class NamedEntity(Entity):
    """This is a super class for all entities that carry a name."""
    def __init__(self, name):
        super(NamedEntity, self).__init__()
        self.name = name
        
        
class Passenger(Entity):
    """A Passenger object represents a person who can be booked on flights."""
    
    def __init__(self, first_name, last_name):
        """Creates a new passenger with the given first and last name, having an initial ago of zero.
        :param firstname: the first name of the passenger.
        :param lastname: the last name of the passenger.
        """
        super(Passenger, self).__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.age = 0
        
class Flight(NamedEntity):
    """A Flight represents the opportunity to travel from one airport to another.
    Each Flight is executed using a particular type of airplane and holds a limited amount of passengers.
    """
    
    def __init__(self, name):
        """Creates a new flight with the given name.
        :param name: the new name for the flight.
        """
        super(Flight, self).__init__(name)
        self.__airplane = None
        self.passenger_ids = []
        self.__free_seats = 0

    @property
    def airplane(self):
        return self._airplane
    
    @airplane.setter
    def airplane(self, value):
        self.__airplane = value
        self.__free_seats = value.total_seats
        
    @property
    def free_seats(self):
        return self.__free_seats - len(self.passenger_ids)
    
    @free_seats.setter
    def free_seats(self, value):
        self.__free_seats = value
    
    def has_passenger(self, passenger):
        return passenger.id in self.passenger_ids
    
    def add_passenger(self, passenger):
        self.passenger_ids.append(passenger.id)
        
    def remove_passenger(self, passenger):
        if passenger.id in self.passenger_ids:
            self.passenger_ids.remove(passenger.id)
            return True
        return False
    

class AirplaneType(NamedEntity):
    """An AirplaneType represents a specific typo of airplane which is
    characterized by its name and a number of total seats.
    """
    
    def __init__(self, name):
        """Creates a new AirplaneType entity with the given name.
        :param name: the name of the type of airplane.
        """
        super(AirplaneType, self).__init__(name)
        self.total_seats = 0
    
    
        
    
        
