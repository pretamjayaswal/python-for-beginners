
class Employee():

    raise_amount = 1.04
    no_of_emp = 0

    def __init__(self, first,last, pay):
        self.first = first
        self.last = last
        self.email = first+'_'+last+'@company.com'
        self.pay = pay
        Employee.no_of_emp += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
        # return 'JJJHJJ'
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    
    @classmethod
    def set_raise_amount(cls,amount):
        cls.raise_amount = amount
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


class Developer(Employee):
    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay) #or
        # Employee.__init__(first,last,pay)

        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self,first,last,pay,employees=None):
        super().__init__(first,last,pay) #or
        # Employee.__init__(first,last,pay)

        self.employees = [] if employees else employees

    

emp1 = Developer('pritam', 'jayaswal', 20000, 'Python')
emp2 = Developer('ketan', 'singh', 10000, 'Javascript')

print(emp1.prog_lang)




