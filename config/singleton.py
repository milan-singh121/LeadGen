"""
Purpose: This script defines the singleton class,
a design pattern where only a single instance of a class can be created.
"""


class Singleton(type):
    """
    Singleton metaclass to ensure only one instance of the class is created.
    This metaclass is meant to be used as a parent class for the actual class definition.
    """

    # Dictionary to store instances of the classes
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        This method is called when the class is instantiated.

        Args:
            *args: Variable length argument list
            **kwargs: Arbitrary keyword arguments

        Returns:
            The existing instance of the class if it already exists, else creates a new instance.
        """

        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
