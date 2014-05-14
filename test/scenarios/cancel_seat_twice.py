from natspec_utils.stringutils import stringToUnicode as u;

import unittest
from test.support import TestSupport
from service.airline_service import AirlineService
from persistence.in_memory_context import InMemoryPersistenceContext

class CancelSeatTwice(unittest.TestCase):
    """This class serves as a template for all classes that are generated for
    NatSpec scenarios (.natspec files). It is recognized by NatSpec based on its
    special name and applies to all scenarios in the same package and all sub
    packages (unless there is another template class in one of the sub packages).
    This particular template is a unittest test case where the concrete steps of the
    test are filled by the NatSpec code generator.
    """
    
    def setUp(self):
        """Sets up the test environment (i.e., initialize the service class, the
        entity manager and the test support class).
        """
        self.service = AirlineService()
        self.persistence_context = InMemoryPersistenceContext()
        self.test_support = TestSupport(self.service, self.persistence_context, self)
        
    def test(self):
        """
         The code in this method is generated from: /de.devboost.natspec.example.python/test/scenarios/cancel_seat_twice.natspec
         Never change this method or any contents of this file, all local changes will we overwritten.
        """
        # Given an airplane Boeing-737-600
        airplaneType_Boeing_737_600 = self.test_support.given_an_airplane(u("Boeing-737-600"))
        
        # Given a flight LH-1234
        flight_LH_1234 = self.test_support.given_a_flight(u("LH-1234"))
        
        # that is executed using a Boeing-737-600
        self.test_support.that_is_executed_using_a(u("Boeing-737-600"), flight_LH_1234)
        
        # With 2 free seats
        self.test_support.with_free_seats(2, flight_LH_1234)
        
        # Given a passenger John Doe
        passenger_John_Doe = self.test_support.given_a_passenger(u("John"), u("Doe"))
        
        # Book seat for John Doe at LH-1234
        operationStatus_John_Doe_LH_1234 = self.test_support.book_seat_for(u("John"), u("Doe"), u("LH-1234"))
        
        # Assume a valid ticket is issued
        self.test_support.assume_valid_ticket(operationStatus_John_Doe_LH_1234)
        
        # Cancel seat for John Doe at LH-1234
        operationStatus_John_Doe_LH_12340 = self.test_support.cancel_seat_for(u("John"), u("Doe"), u("LH-1234"))
        
        # Assume a valid ticket is issued
        self.test_support.assume_valid_ticket(operationStatus_John_Doe_LH_12340)
        
        # Cancel seat for John Doe at LH-1234
        operationStatus_John_Doe_LH_12341 = self.test_support.cancel_seat_for(u("John"), u("Doe"), u("LH-1234"))
        
        # Assume no valid ticket is issued
        self.test_support.assume_no_valid_ticked_is_issued(operationStatus_John_Doe_LH_12341)
        
        
        
if __name__ == '__main__':
    unittest.main()