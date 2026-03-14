class a:
    def __init__(self):
        print("Class a")
        
class b(a):
    def __init__(self):
        super().__init__()
        print("Inside class B")
obj=b()
