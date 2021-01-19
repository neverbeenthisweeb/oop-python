class Customer:
    def __init__(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type

    def update_membership(self, new_membership):
        print("Calculating costs...")
        self.membership_type = new_membership

    def __str__(self):
        return self.name + " " + self.membership_type

    def print_all_customers(customers):
        for customer in customers:
            print(customer)

    # by default __eq__ compares by memory address
    def __eq__(self, other):
        if self.name == other.name and self.membership_type == other.membership_type:
            return True
        return False

    # TODO: Read more about hashing.
    __hash__ = None

    # repr stands for representation (probably?)
    # TODO: Read more about __repr__.
    __repr__ = __str__


customers = [Customer("Caleb", "Bronze"), Customer("Brad", "Silver")]

print(customers[1])
customers[1].update_membership("Gold")
print(customers[1])

# static method
Customer.print_all_customers(customers)

customers = [Customer("Caleb", "Bronze"), Customer("Caleb", "Bronze")]

# comparing depends on __eq__ method
print(customers[0] == customers[1])

# printing depends on __repr__ method
print(customers)
