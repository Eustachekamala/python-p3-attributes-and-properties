#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name: str, job: str):
        self._name = ""
        self._job = ""
        self.name = name
        self.job = job
    
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, value : str):
        if isinstance (value, str) and 1 <= len(value) <= 25:
            return value
        else:
            print("Name must be a string between 1 and 25 characters.")
    
    @property
    def job(self) -> str:
        return self._job
    
    @job.setter
    def job(self, value: str):
        if isinstance (value, str) and value in APPROVED_JOBS:
            return value
        else:
            print("Job must be in list of approved jobs.")
        

person1 = Person("Jeack",job="Legal")