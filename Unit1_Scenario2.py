class Employee:

    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    def category(self):
        if self.salary >= 70000:
            return "High Salary"
        elif self.salary >= 40000:
            return "Medium Salary"
        return "Low Salary"


class Company:

    def __init__(self):
        self.employees = []

    def add(self, emp):
        self.employees.append(emp)

    def display(self):
        for e in self.employees:
            print(e.id, e.name, e.salary, e.category())


c = Company()

c.add(Employee(101, "Sayam", 75000))
c.add(Employee(102, "Rahul", 55000))
c.add(Employee(103, "Amit", 30000))

c.display()
