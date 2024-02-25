# Define a class using explicit getters and setters
class PersonWithGetSet:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_name(self):
        # Getter method for the name
        return self._name

    def set_name(self, value: str):
        # Setter method for the name
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            raise ValueError("Name must be a non-empty string")
        
    def get_age(self):
        # Getter method for the age
        return self._age
    
    def set_age(self, value: int):
        # Setter method for the age
        if isinstance(value, int) and value >= 0:
            self._age = value
        else:
            raise ValueError("Age must be a non-negative integer")
    

# Define a class using @property and @setter
class PersonWithProperty:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        # Property (getter) for the name
        return self._name

    @name.setter
    def name(self, value: str):
        # Setter for the name
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            raise ValueError("Name must be a non-empty string")
        
    @property
    def age(self):
        # Property (getter) for the age
        return self._age
    
    @age.setter
    def age(self, value: int):
        # Setter for the age
        if isinstance(value, int) and value >= 0:
            self._age = value
        else:
            raise ValueError("Age must be a non-negative integer")

# Demonstration
if __name__ == "__main__":
    # Using class with explicit getters and setters
    person1 = PersonWithGetSet("John", 30)
    print(person1.get_name(), person1.get_age())
    person1.set_name("Bob")
    person1.set_age(35)
    print(person1.get_name(), person1.get_age())

    # Using class with @property and @setter
    person2 = PersonWithProperty("Marie", 40)
    print(person2.name, person2.age)
    person2.name = "Diana"
    person2.age = 45
    print(person2.name, person2.age)