class myClass:
    
    def __init__(self,value):
        self.value = value
        
    def get_value(self):
        return self.value
    
    def set_value(self,value):
        self.value=value 

obj = myClass(10)
print(obj.get_value())
obj.set_value(20)
print(obj.get_value()) 