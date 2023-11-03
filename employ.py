# define the employee class as employ
class Employ:
    # define initialize method that accepts name, id, department, and job title
    def __init__(self, name, id_number, department, job_title):
        # setting name to a variable
        self.__name = name
        # setting id number to a variable
        self.__id_number = id_number
        # setting department to a variable
        self.__department = department 
        # setting job title to a variable 
        self.__job_title = job_title
    # define a function to change the name
    def set_name(self, name):
        # assign name to a variable
        self.__name = name 
    # define the method to set employee ID
    def set_id(self, id_number):
        # assign id_number to a variable
        self.__id_number = id_number
    # define method to set the department 
    def set_department(self, department):
        # assign deprtment to a variable 
        self.__department = department
    # method to set job title 
    def set_job_title(self, job_title):
        # assign job title to a variable
        self.__job_title = job_title 
    # method to return name
    def get_name(self):
        # return name variable
        return self.__name
    # method to get ID
    def get_id(self):
        # return the ID variable 
        return self.__id_number
    # get the department method
    def get_department(self):
        # return name variable
        return self.__department
    # return job title method
    def get_job_title(self):
        # return the name 
        return self.__job_title
    # define str method
    def __str__(self):
        # return a f string of the objects attributes
        return f'Name: {self.__name}\n' \
        f'ID Number: {self.__id_number}\n' \
        f'Department: {self.__department}\n' \
        f'Job Title: {self.__job_title}\n'