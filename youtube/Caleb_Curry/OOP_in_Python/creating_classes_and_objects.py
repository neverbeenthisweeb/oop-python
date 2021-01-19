class Customer:
    # __init__ is also known as:
    # - constructor
    # - initializer
    #
    # "self" is the same as "this" in other programming languages
    def __init__(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type


customers = [Customer("Caleb", "Bronze"), Customer("Brad", "Silver")]

print(customers[1].name)
