class Person:
    # name = "Sriam"
    # occupation = "software Dev"
    # newworth = 10
    
    def info(self):
        print(f"{self.name} is a {self.occupation}")
    
a = Person()
a.name="Pritam"
a.occupation="Hr"
b=Person()
b.name="Akash"
b.occupation="Farmer"
b.info()
a.info()