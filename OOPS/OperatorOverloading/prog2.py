import math
class demo:
    def sample(self,x=None,y=None,z=None):
        if(x!=None and y!=None and z!=None):
            print (x+y+z)
        elif(x!=None and y!=None):
            print (x+y)
        else:
            print (int(math.sqrt(x)))
            
s=demo()
s.sample(3,4,5)
s.sample(3,4)
s.sample(81)