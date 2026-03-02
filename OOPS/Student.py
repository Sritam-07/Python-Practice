class Student:
    tns=0
    def set_student_details(self,sid,sname,smno):
        self.sid = sid
        self.sname = sname
        self.smno = smno
    @classmethod
    def set_total_students_joined(cls):
        cls.tns=cls.tns+1
        
    def get_student_details(self):
        print(f"The student id is : {self.sid}")
        print(f"The student name is : {self.sname}")
        print(f"The student id is : {self.smno}")  
        
s1=Student()
s1.set_student_details(101,"sritam","75069506436")
s1.get_student_details()

        
        
    