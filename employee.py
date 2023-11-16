class Employee:

    def __init__(self, name, number):
        self.__name = name
        self.__number = number 

    def set_name(self, name):
        self.__name = name 

    def set_number(self, number):
        self.__number = number

    def get_name(self):
        return self.__name
    
    def get_number(self):
        return self.__number
    
class ProductionWorker(Employee):

    def __init__(self, name, number, shift, pay):

        Employee.__init__(self, name, number)

        self.__shift = shift
        self.__pay = pay 
    
    def set_shift(self, shift):
        self.__shift = shift 

    def set_pay(self, pay):
        self.__pay = pay

    def get_shift(self):
        if self.__shift == 1:
            return 'Day Shift'
        elif self.__shift == 2:
            return 'Night Shift'
        else:
            return 'Shift Not Found'
    
    def get_pay(self):
        return self.__pay 
    
class ShiftSupervisor(Employee):

    def __init__(self, name, number, salary, bonus):
        Employee.__init__(self, name, number)

        self.__salary = salary 
        self.__bonus = bonus

    def set_salary(self, salary):
        self.__salary = salary 

    def set_bonus(self, bonus):

        self.__bonus = bonus
    


    def get_salary(self):
        return self.__salary
    
    def get_bonus(self):
        if self.__bonus == 'y' or self.__bonus == 'Y':
            return (int(self.__salary) * .05)
        else:
            return 'No Bonus Earned'
        
    