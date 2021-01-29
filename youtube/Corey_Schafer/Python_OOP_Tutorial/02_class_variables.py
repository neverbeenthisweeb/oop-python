class Employee:
    # class variables
    num_of_employees = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        # instance variables
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@company.com"
        Employee.num_of_employees += 1

    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


print(Employee.num_of_employees)
emp_1 = Employee("Corey", "Schafer", 100)
emp_2 = Employee("Anton", "Michael", 100)
# NOTE: Number of employees will be increased by +2.
print(Employee.num_of_employees)


# NOTE: What happened in background is:
# Check if instance has corresponding attribute. Else,
# check if class has corresponding attribute.
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# NOTE: As you can see, no .raise_amount is shown in emp_1 and
# emp_2. Previously, we are using class' .raise_amount attribute.
print(Employee.__dict__)
print(emp_1.__dict__)
print(emp_2.__dict__)

# NOTE: Here, we are adding a new instance attribute.
emp_1.raise_amount = 2.00
print(emp_1.__dict__)
