# NOTE: Python helpful paradigm --> "Don't use it if you don't need it."
# NOTE: "_" prefix means private (i.e. "_name", "_address")

class User:
    def log(self):
        print(self)


class Teacher(User):
    def log(self):
        print("I am a teacher!")


class Customer(User):
    def __init__(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type

    # Pythonic getter and setter
    # https://stackoverflow.com/a/36943813/11835549
    @property
    def name(self):
        print("getting name...")
        return self._name

    @name.setter
    def name(self, name):
        print("setting name...")
        self._name = name

    @name.deleter
    def name(self):
        print("deleting name...")
        del self._name

    def __str__(self):
        return self.name + " " + self.membership_type


customers = [Customer("Caleb", "Gold"), Customer("Brad", "Silver"), Teacher()]

# encapsulation
# del customers[0].name
print(customers[0].name)

# inheritance
customers[0].log()

# polymorphism
# NOTE: Probably it relates with Liskov Substitution Principle.
# TODO: Read more about about Polymorphism X Liskov Substitution Principle.
for c in customers:
    c.log()
