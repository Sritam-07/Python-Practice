class Teacher:
    def set_id(self,id):
        self.id=id
        
    def set_name(self,name):
        self.name=name
        
    def set_adr(self,adr):
        self.adr=adr
    
    def set_sal(self,sal):
        self.sal=sal
    
    def get_id(self):
        print(self.id)
        
    def get_name(self):
        print(self.name)
        
    def get_adr(self):
        print(self.adr)
    
    def get_sal(self):
        print(self.sal)
    
class student(Teacher):
    def set_fees(self,fees):
        self.fees=fees
    def get_fees(self):
        print(self.fees)
        
t1=Teacher()
t1.set_id(123)
t1.set_adr("Gunupur")
t1.set_sal(2324)
t1.set_name("Rohit")

t1.get_name()
t1.get_id()
t1.get_adr()
t1.get_sal()
print("-------------------------------------------------------------")
s=student()
s.set_id(312)
s.set_fees(324)
s.set_name("Ashutosh")
s.set_adr("bali")

s.get_name()
s.get_id()
s.get_adr()
s.get_fees()

    