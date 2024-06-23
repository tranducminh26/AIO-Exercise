from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name, yob):
        self._name = name
        self._yob = yob
        
    def get_yob(self):
        return self._yob
    
    @abstractmethod   
    def describe(self):
        pass


class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name=name, yob=yob)
        self.__grade = grade
    
    def describe(self):
        print(f'Student-Name: {self._name} - YoB: {self._yob} - Grade: {self.__grade}')
    

class Doctor(Person):
    def __init__(self, name, yob, specialist):
        super().__init__(name=name, yob=yob)
        self.__specialist = specialist
    
    def describe(self):
        print(f'Doctor - Name: {self._name} - YoB: {self._yob} - Specialist: {self.__specialist}')
        
    
class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name=name, yob=yob)
        self.__subject = subject
    
    def describe(self):
        print(f'Teacher - Name: {self._name} - YoB: {self._yob} - Subject: {self.__subject}')
        
    
class Ward:
    def __init__(self, name):
        self.__name = name
        self.__list_people = []
    
    def add_person(self, person):
        self.__list_people.append(person)
    
    def describe(self):
        print(f'Ward Name: {self.__name}')
        for p in self.__list_people:
            p.describe()
    
    def count_doctor(self):
        counter = 0
        for p in self.__list_people:
            if isinstance(p, Doctor):
                counter += 1
        return counter

    def sort_age(self):
        self.__list_people.sort(key=lambda x: x.get_yob(), reverse=True)
        
    def compute_average(self):
        total = 0
        counter = 0
        for p in self.__list_people:
            if isinstance(p, Teacher):
                total += p.get_yob
                counter += 1
        return total / counter  