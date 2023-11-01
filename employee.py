class Employee:
    def __init__(self, name, id_number, department, job_title):
        self.__name = name
        self.__id_number = id_number
        self.__department = department 
        self.__job_title = job_title

    def set_name(self, name):
        self.__name = name 

    def set_id(self, id_number):
        self.__id_number = id_number
    
    def set_department(self, department):
        self.__department = department

    def __str__(self):
        return f'Name: {self.__name}\n' \
        f'ID Number: {self.__id_number}\n' \
        f'Department: {self.__department}\n' \
        f'Job Title: {self.__job_title}'