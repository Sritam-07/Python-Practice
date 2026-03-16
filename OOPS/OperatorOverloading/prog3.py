class Commercial:
    def set_values(self,mtno,nou):
        self.mtno=mtno
        self.nou=nou
    
    def calculate_bill(self):
        self.amount = (7.70*self.nou)
    
    def display_Values(self):
        print(self.mtno)
        print(self.nou)
        print(self.amount)
        
class Domestic(Commercial):
    def calculate_bill(self):
        self.amount=(5.50*self.nou)
    
obj1=Commercial()
obj2=Domestic()

obj1.set_values(12,200)
obj1.calculate_bill()
obj1.display_Values()

obj2.calculate_bill()
