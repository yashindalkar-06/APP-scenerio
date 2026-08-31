class Course:

    def __init__(self, name, duration, fee):
        self.name = name
        self.duration = duration
        self.fee = fee

    def category(self):
        if self.duration <= 6:
            return "Short-Term"
        return "Long-Term"


class Institute:

    def __init__(self):
        self.courses = []

    def add(self, course):
        self.courses.append(course)

    def display(self):
        for c in self.courses:
            print(c.name, c.duration, "months", c.fee, c.category())


i = Institute()

i.add(Course("Python", 3, 5000))
i.add(Course("Data Science", 12, 20000))
i.add(Course("Web Development", 6, 10000))

i.display()
