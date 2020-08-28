from datetime import datetime, date


class Employee:
    def __init__(self, name, surname, email, phone, salary):
        self.name = name
        self.surname = surname
        self.email = email
        self.phone = phone
        self.salary = salary

    def work(self):
        return 'I came to the office'

    def salary_check(self, salary, days):
        return salary * days

    def __lt__(self, other):
        return self.salary < other.salary

    def __gt__(self, other):
        return self.salary > other.salary

    def __eq__(self, other):
        return self.salary == other.salary

    def check_salary(self, salary):
        quantity_of_days = date.today() - date(year=date.today().year, month=date.today().month, day=1)
        quantity_of_weeks = (quantity_of_days.days + 1) // 7
        quantity_of_days_offs = quantity_of_weeks * 2
        quantity_of_business_days = quantity_of_days.days - quantity_of_days_offs
        return quantity_of_business_days * salary


employee_one = Employee('John', 'Smith', 'johnsmith@mail.com', '30583258205', '300')


print(employee_one.salary_check(300, 5))

class Recruiter(Employee):

    def __init__(self, name, surname, email, phone, salary, hired_this_month):
        Employee.__init__(self, name, surname, email, phone, salary)
        self.hired_this_month = hired_this_month

    def work(self):
        return super().work() + 'and start hiring'

    def __str__(self):
        return 'Recruiter : ' + self.name.capitalize() + ' ' + self.surname.capitalize()


recruiter_one = Recruiter('mary', 'james', 'maryjames@mail.com', '932569357', '500', '5')
recruiter_two = Recruiter('liza', 'black', 'lizablack@mail.com', '836438562', '400', '10')


print(recruiter_one.check_salary(400))


class Programmer(Employee):

    def __init__(self, name, surname, email, phone, salary, tech_stack, closed_this_month):
        Employee.__init__(self, name, surname, email, phone, salary)
        self.tech_stack = tech_stack
        self.closed_this_month = int(closed_this_month)

    def work(self):
        return super().work() + 'and start programing'

    def __str__(self):
        return 'Programmer : ' + self.name.capitalize() + ' ' + self.surname.capitalize()

    def __lt__(self, other):
        return self.tech_stack < other.tech_stack

    def __gt__(self, other):
        return self.tech_stack > other.tech_stack

    def __eq__(self, other):
        return self.tech_stack == other.self_stack

    def alfa_programmer(self, other):
        return set(self.tech_stack + other.tech_stack), self.closed_this_month + other.closed_this_month


programmer_one = Programmer('mick', 'colins', 'nickcolins@mail.com', '823659256', '600', ['Java', 'C#', 'C++'], '5')
programmer_two = Programmer('leo', 'luck', 'leoluck@mail.com', '283569234', '450', ['Python', 'Java', 'PHP', 'Swift'], '10')

print(programmer_one.alfa_programmer(programmer_two))
