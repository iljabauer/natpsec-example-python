from service.validation.support import ValidationSupport

class _NatSpecTemplate(object):
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
        """ @MethodBody """
        return self.validation_support.status