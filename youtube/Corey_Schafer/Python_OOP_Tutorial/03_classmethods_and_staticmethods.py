import datetime


class Employee:
    num_of_employees = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@company.com"
        Employee.num_of_employees += 1

    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    # NOTE: Sometimes, classmethod can also be used as a constructor.
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    # NOTE: Simply put, if we are not using any class variable, we set it
    # as a static method.
    @staticmethod
    def is_workday(day):
        # NOTE:
        # Monday, ... , Saturday, Sunday
        # 0, ... , 5, 6
        if day.weekday() >= 5:
            return False
        return True


emp_1 = Employee("Corey", "Schafer", 100)
emp_2 = Employee("Anton", "Michael", 100)

emp_str_3 = 'John-Rascal-200'
emp_3 = Employee.from_string(emp_str_3)

Employee.set_raise_amount(1.05)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(emp_3.raise_amount)

dt = datetime.date(2016, 7, 10)
print(Employee.is_workday(dt))

dt = datetime.date(2016, 7, 11)
print(Employee.is_workday(dt))
