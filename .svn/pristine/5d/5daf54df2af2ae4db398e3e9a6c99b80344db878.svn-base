from service.validation.rules import Rules
from service.status import OperationStatus

class AirlineService(object):
    """The AirlineService provides very basic business functionality for the
    airline domain. It allows to book seats for passengers on flights
    and to cancel these seats.
    """
    
    def book_seat(self, passenger, flight):
        """Tries to book a seat for the given passenger on the given flight. Before
        the seat is actually booked some validation rules are checked to make
        sure the constraints of the domain (e.g., that a passenger can book at
        most one seat for a flight) are met. If one of the validation rules is
        violated, this operation fails.
        :param flight: the flight to book the seat on.
        :param passenger: the passenger to book the seat for.
        :returns: a status object representing the operations success (or failure).
        """
        rules = Rules(flight, passenger)
        status = rules.validate()
        if status.valid:
            flight.add_passenger(passenger)
        return status
    
    def cancel_seat(self, passenger, flight):
        """Cancels the seat booked by the given passenger on the given flight. This
        operation can fail if the passenger has not booked a seat on the given
        flight.
        :param passenger: the passenger to cancel the seat for.
        :param flight: the flight to cancel the seat on.
        :returns: a status object representing the operations success (or failure).
        """
        if flight.remove_passenger(passenger):
            return OperationStatus("Passenger was removed", True)
        return OperationStatus("Passenger was not booked on flight", False)