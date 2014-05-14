from service.validation.support import ValidationSupport

class Rules(object):
    """This class serves as a template for validation rule classes that are written
    in plain natural language. The template is instantiated by NatSpec for all
    the .natspec files in this package. The @MethodBody placeholder
    in validate() is replaced with the code that performs the actual validation.
    See class Rules for a concrete example validation class.
    This class is an example of applying NatSpec for non-testing purposes.
    """
    def __init__(self, flight, passenger):
        self.validation_support = ValidationSupport(flight, passenger)
        
    def validate(self):
        """Checks that all validation rules are met.
        :returns: the status of the validation (i.e., success or failure).
        """        
        """
         The code in this method is generated from: /de.devboost.natspec.example.python/service/validation/rules.natspec
         Never change this method or any contents of this file, all local changes will we overwritten.
        """
        # There needs to be a free seat for the passenger.
        self.validation_support.check_free_seats()
        
        # There should be at least 0 free seats to handle overbooking.
        self.validation_support.check_free_seats_with_buffer(0)
        
        # Each Passenger can only be booked once.
        self.validation_support.check_unique_passenger()
        
        
        return self.validation_support.status