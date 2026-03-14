class java_book:
    def __init__(self,page):
        self.page=page
class math_book:
    def __init__(self,page):
        self.page=page
        
    def __add__(self, x):
        print(self.page+x.page)

m=java_book(700)
j=math_book(1200)
m+j
        
