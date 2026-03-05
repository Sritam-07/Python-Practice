class StudentsMarks:
    clg_name="GIETU"
    pass_marks=40
    def set_student_details(self,sid,marks):
        self.id=sid
        self.smarks=marks
        
    @classmethod
    def get_college_details(cls):
        print(f"The College name is : {cls.clg_name}")
        print(f"The pass Marks is {cls.pass_marks}")
    
    def get_student_details(self):
        print(f"The student id is {self.id}")
        print(f"The student Mark is {self.smarks}")
        

s1=StudentsMarks()
s1.set_student_details(122,40)
s2=StudentsMarks()
s2.set_student_details(123,45)
print("Student 1 detail : ")
s1.get_student_details()
print("Student 2 detail : ")
s2.get_student_details()
StudentsMarks.get_college_details()
