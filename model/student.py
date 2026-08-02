from datetime import datetime

class Student:
    """Student Class
    """
    
    # default constructor
    def __init__(self, student_id=None, name="", date_of_admission=None):
        self._student_id = student_id
        self._name = name
        self._date_of_admission = date_of_admission
        
    # Alternative constructor
    @classmethod
    def from_id_name(cls, name, student_id):
        return cls(name, student_id, datetime.today())
    
    # Alternative constructor
    @classmethod
    def empty_class(cls):
        return cls()
    
    # getter and setter for student id
    @property
    def student_id(self):
        return self._student_id
    
    @student_id.setter
    def student_id(self, value):
        self._student_id = value
        
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
        
    # getter and setter for date of admission
    @property
    def date_of_admission(self):
        return self._date_of_admission
    
    @date_of_admission.setter
    def date_of_admission(self, value):
        self._date_of_admission = value
        
    def __str__(self):
        return(
            f"Student ID: {self._student_id}, "
            f"Name: {self.name}, "
            f"Date of admission: {self.date_of_admission.strftime('%m/%d/%Y')}"
        )
    
