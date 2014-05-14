from service.status import OperationStatus
from natspec_utils.decorators import TextSyntax
class ValidationSupport():
    """The ValidationSupport call defined all methods that are required to
    execute the textual validation rules present in this example.
    """
        
    def __init__(self, flight, passenger):
        """Creates a new instance of this class that can be used to validate the
        given flight and passenger.
        
        :param flight: the flight to validate.
        :param passenger: the passenger to validate.
        """
        self.flight = flight
        self.passenger = passenger
        self.status = OperationStatus()
        
    def set_invalid(self, msg):
        """Sets the status of this validation to invalid (failure) and adds the given message.
        :param msg: the message to add.
        """
        self.status.valid = False
        self.status.msg = msg
        
    @TextSyntax("Each Passenger can only be booked once.")
    def check_unique_passenger(self):
        """Checks that the passenger has not already booked a seat on this flight."""
        if self.passenger.id in self.flight.passenger_ids:
            self.set_invalid("A passenger can only be booked once for each flight.")
            
    @TextSyntax("There should be at least #1 free seats to handle overbooking.", types=["int"])
    def check_free_seats_with_buffer(self, overbooking_buffer):
        """Checks that the given number of seats is held free."""
        if self.flight.free_seats < overbooking_buffer:
            self.set_invalid("There are no free seats for the flight.")
            
    @TextSyntax("There needs to be a free seat for the passenger.")
    def check_free_seats(self):
        """Checks that there is at least one seat available."""
        if self.flight.free_seats < 1:
            self.set_invalid("There are no free seats for the flight.")
            
    @TextSyntax("The Passenger needs to be at least #1 years old.", types=["int"])
    def passenger_needs_to_be_at_least_years_old(self, minimal_age):
        """Checks that the passenger has at least the given age (in years)."""
        if self.passenger.age < minimal_age:
            self.set_invalid("The passenger needs to be at least {0} years.".format(minimal_age))
        
    
