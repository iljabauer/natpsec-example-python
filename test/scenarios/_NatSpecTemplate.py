import unittest
from test.support import TestSupport
from service.airline_service import AirlineService
from persistence.in_memory_context import InMemoryPersistenceContext

class _NatSpecTemplate(unittest.TestCase):
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
        """ @MethodBody """
        
if __name__ == '__main__':
    unittest.main()