# create a Employee class
class Employee:
    #define inisialize method and pass name and number to the object
    def __init__(self, name, number):
        # sets name to a varible only accessable by instance of object
        self.__name = name
        # set number to a variable
        self.__number = number 
    # mutator method to set name
    def set_name(self, name):
        # set name to variable
        self.__name = name 
    # mutator method to set number
    def set_number(self, number):
        # set number to variable
        self.__number = number
    # accessor method to get name 
    def get_name(self):
        # return name
        return self.__name
    # accessor method to get number
    def get_number(self):
        # return number 
        return self.__number
# define ProductionWorker subclass of Employee   
class ProductionWorker(Employee):
    # define initialize method and pass name, number, shift, and pay to the object
    def __init__(self, name, number, shift, pay):
        # create the superclass method
        Employee.__init__(self, name, number)
        # set subclass datat attributes
        # set shift
        self.__shift = shift
        # set pay 
        self.__pay = pay 
    # mutator method to set shift 
    def set_shift(self, shift):
        # set shift to data attribute
        self.__shift = shift 
    # mutator method to set pay/salary
    def set_pay(self, pay):
        # set pay
        self.__pay = pay
    # accessor method to get shift worked
    def get_shift(self):
        # if statement to determine what shift string to return 
        if self.__shift == 1:
            # return day shift if integer is 1
            return 'Day Shift'
        # elif for is integer is 2 return night shift 
        elif self.__shift == 2:
            # return nightshift 
            return 'Night Shift'
        # else statement to return shift not found if not 1 or 2 input 
        else:
            # return string if shift not entered
            return 'Shift Not Found'
    # accessor method to get pay
    def get_pay(self):
        # return pay
        return self.__pay 
# define ShiftSupervisor class a subclass of Employee
class ShiftSupervisor(Employee):
    # define the initialize statement 
    def __init__(self, name, number, salary, bonus):
        # create the superclass object to inherit from 
        Employee.__init__(self, name, number)
        # set salary to data attribute
        self.__salary = salary 
        # set bonus 
        self.__bonus = bonus
    # mutator method to set salary
    def set_salary(self, salary):
        # set salary
        self.__salary = salary 
    # mutator method to set bonus
    def set_bonus(self, bonus):
        # set bonus
        self.__bonus = bonus
    # accessor method to return salary
    def get_salary(self):
        # return salary
        return self.__salary
    # accessor method to return the bonus 
    def get_bonus(self):
        # if statement to determine if bonus quota is met
        if self.__bonus == 'y' or self.__bonus == 'Y':
            # return 5% of salary as bonus
            return (int(self.__salary) * .05)
        # if bonus not earned return no bonus
        else:
            # return no bonus 
            return 'No Bonus Earned'
        
    