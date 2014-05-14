from natspec_utils.decorators import TextSyntax


class TestSupport(object):
    """This class contains all test support methods that are required to make the
    example specifications executable. Methods that are decorated with the
    TextSyntax decorator are recognized by NatSpec.
    This class is parameterized by two parameters that are passed to the
    constructor (the service class which implements the business logic and the
    entity manager that provides access to all entities).
    """
        
    def __init__(self, service, persistence_context, test_case):
        """Creates a new {@link TestSupport} instance. This constructor is usually 
        invoked from a {@link _NatSpecTemplate}.
        :param service: the business service logic.
        :param persistence_context: the entity manager to access entities.
        :param test_case: the test case we are running, needed to access asserts
        """
        self.service = service
        self.persistence_context = persistence_context
        self.test_case = test_case
        self.passengers = {}
        self.flights = {}
        self.airplane_types = {}

    @TextSyntax(["Given a Passenger #1 #2"], types=["str", "str"], return_type="Passenger")
    def given_a_passenger(self, first_name, last_name):
        """Creates a new passenger.
        :param first_name: the first name of the passenger.
        :param last_name: the last name of the passenger.
        :returns: the newly created passenger.
        """
        passenger = self.persistence_context.create_passenger(first_name, last_name)
        self.passengers.update({"{0} {1}".format(first_name, last_name): passenger})
        return passenger

    @TextSyntax("With age of #2 years", types=["Passenger", "int"])
    def with_age_of_years(self, passenger, age):
        """Sets the age of the given passenger. The passenger is expected to be
        contained in the implicit context (i.e., it must be created by a previous
        sentence/test support method). The name of the passenger is not
        explicitly required here, because there is no placeholder for the
        passenger parameter (i.e., #1 is missing).
        :param passenger: the passenger to set the age for.
        :param age: the new age for the passenger.
        """
        passenger.age = age

    @TextSyntax(["Given an Airplane #1"], types=["str"], return_type="AirplaneType")
    def given_an_airplane(self, name):
        """Creates a new type of airplane.
        :param name: the name of the type of airplane.
        :returns: the newly created airplane type.
        """
        airplane_type = self.persistence_context.create_airplane_type(name)
        self.airplane_types.update({name: airplane_type})
        return airplane_type

    @TextSyntax(["Given a flight #1"], types=["str", ], return_type="Flight")
    def given_a_flight(self, name):
        """Creates a new flight.
        :param name: the name of the flight.
        :returns: the newly created flight.
        """
        flight = self.persistence_context.create_flight(name)
        self.flights.update({name: flight})
        return flight

    @TextSyntax("that is executed using a #1", types=["str", "Flight"])
    def that_is_executed_using_a(self, airplane_name, flight):
        """Assigns the type of airplane that is used to execute the last mentioned flight.
        :param airplane_name: the type of airplane to assign to the flight.
        :param flight: the flight for which to set the airplane type (must be available from context).
        """
        airplane = self.airplane_types.get(airplane_name)
        flight.airplane = airplane

    @TextSyntax("With #1 free seats", types=["int", "Flight"])
    def with_free_seats(self, free_seats, flight):
        """Sets the number of free seats for the flight mentioned last.
        :param free_seats: the number of free seats
        :param flight: the flight to set the seats for (must be available from context).
        """
        flight.free_seats = free_seats

    @TextSyntax("Book seat for #1 #2 at #3", types=["str", "str", "str"], return_type="OperationStatus")
    def book_seat_for(self, first_name, last_name, flight_name):
        """Tries to book a seat for the given passenger on the given flight.
        :param first_name: the first name of passenger to book the flight for
        :param last_name: the last name of passenger to book the flight for
        :param flight_name: the name of flight to book the seat on.
        :returns: the status of the booking operation which can be validated using
                  assume_valid_ticket(OperationStatus) or
                  assume_no_valid_ticked_is_issued(OperationStatus).
        """
        passenger = self.passengers.get("{0} {1}".format(first_name, last_name))
        flight = self.flights.get(flight_name)
        return self.service.book_seat(passenger, flight)

    @TextSyntax("Cancel seat for #1 #2 at #3", types=["str", "str", "str"], return_type="OperationStatus")
    def cancel_seat_for(self, first_name, last_name, flight_name):
        """Tries to cancel the given passenger on the given flight.
        :param first_name: the first name of passenger to book the flight for
        :param last_name: the last name of passenger to book the flight for
        :param flight_name: the name of flight to book the seat on.
        :returns: the status of the cancel operation which can be validated using
                  assume_valid_ticket(OperationStatus) or
                  assume_no_valid_ticked_is_issued(OperationStatus).
        """
        passenger = self.passengers.get("{0} {1}".format(first_name, last_name))
        flight = self.flights.get("{0}".format(flight_name))
        return self.service.cancel_seat(passenger, flight)

    @TextSyntax(["Assume a valid ticket is issued", "Assume cancellation successful"], types=["OperationStatus"])
    def assume_valid_ticket(self, status):
        """Checks that the validity of the last operation is True
        (i.e., that the operation was successful). This method has a TextSyntax decorator
        with multiple patterns (first arg) to map multiple sentences to this method.
        :param status: the status of the last operation (must be implicitly available from context).
        """
        self.test_case.assertTrue(status.valid, msg=status.msg)

    @TextSyntax("Assume no valid ticket is issued", types=["OperationStatus"])
    def assume_no_valid_ticked_is_issued(self, status):
        """Checks that the validity of the last executed business operations is False.
        :param status: the status of the last operation (implicit parameter, not explicitly mentioned in sentence)
        """
        self.test_case.assertFalse(status.valid, msg=status.msg)


    @TextSyntax("Assume #1 has passenger #2", types=["Flight", "Passenger"])
    def assume_has_passenger(self, flight, passenger):
        """Checks that the given passenger is booked for the given flight. Both the
        flight and the passenger must be referenced explicitly.
        :param flight: the flight to check
        :param passenger: the passenger to check
        """
        self.test_case.assertTrue(flight.has_passenger(passenger))
        
        
