from abc import ABC, abstractmethod

class Vehicle(ABC):
    """
    Abstract class representing a general vehicle.

    Abstract classes in Python can contain both abstract methods that must be implemented
    by subclasses and regular methods with default implementation.
    """

    @abstractmethod
    def drive(self):
        """
        Abstract method to drive the vehicle.

        This method must be implemented by any subclass inheriting from this class.

        The use of the @abstractmethod decorator serves several important purposes:
        - It defines a contract for subclasses, indicating that they must implement this method.
        - It prevents the direct instantiation of the Vehicle class. Attempting to instantiate
          Vehicle directly will result in a TypeError, as this abstract method is not implemented.
        - It guides developers in implementing subclasses by clearly marking which methods are
          essential and require overriding.
        - This approach promotes consistent design across subclasses and ensures that each subclass
          provides its own specific implementation of this method, supporting polymorphism.

        """
        pass

    def honk(self):
        """
        Regular method to honk the horn.

        This method has a default implementation and can be inherited as-is by subclasses,
        or it can be overridden for custom behavior in the subclass.
        """
        print("Honking the horn!")

class Car(Vehicle):
    """
    Concrete class representing a car, inheriting from Vehicle.

    This class provides a specific implementation of the abstract methods defined in the
    Vehicle class. It also inherits the honk method, which can be used as-is or overridden.
    """

    def drive(self):
        """
        Implementation of the abstract drive method for a car.
        """
        print("Driving a car.")

# Using the classes
if __name__ == "__main__":
    # Creating an instance of Car and calling the implemented and inherited methods
    my_car = Car()
    my_car.drive()  # Output: Driving a car.
    my_car.honk()   # Output: Honking the horn!

    # Demonstrating that abstract class cannot be instantiated
    try:
        vehicle = Vehicle()
    except TypeError as e:
        print(e)  # Can't instantiate abstract class Vehicle with abstract method drive
