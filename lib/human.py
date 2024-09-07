class Human:
    species = "Homo sapiens"
    
    def __init__(self,age):
        self.age = age
        
    def get_age(self):
        print("Retrieving age")
        return self._age ## => This one is a private attribute
    
    def set_age(self,age):
        if(type(age) in (int, float) and (0 <= age <= 120 )): # => This condition verify, if the of the age is an Int or float
                                                                # That is between 0 and 120
            print(f"Setting age to {age}")
            self._age = age
        else:
            print("Age mut be a Number between 0 and 120")
    
    age = property(get_age, set_age)


guido = Human(age=67)

guido.age = 0

guido.age = False

guido.age = 66

guido.age
    