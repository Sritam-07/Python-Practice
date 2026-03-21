#The main purpose of the constructor is to initialise variable
#The constructor is declared with "__init__(self)"
#It is of 2 types: 1.Parametrised and 2.Non-parametrised constructors
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def get_info(self):
        print(self.name," ",self.age)
    
a=Person(age=12,name="Sritam")
a.get_info()
b=Person("Ayush",17)
b.get_info()