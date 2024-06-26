class InvalideMarks(Exception):
    pass

class Student:
    total_student = 0
    def __init__(self,roll,name,address,mobile):
        Student.total_student += 1
        self.roll = roll
        self.name = name
        self.address = address
        self.mobile = mobile
        
        
    def display_student(self):
        print("Student Details : ")
        print(f"Student name : {self.roll}")
        print(f"Student name : {self.name}")
        print(f"Student name : {self.address}")
        print(f"Student name : {self.mobile}")
        
    def get_total_student(self):
        print(f"Toatal {self.total_student} students having addmission")
        
# s1 = Student(101,'shubham','pune','9874563210')
# s2 = Student(102,'ram','raipur','9874563210')
# s3 = Student(103,'radha','mathura','9874563210')
# print("First Student Details")
# s1.display()
# print("second Student Details")
# s2.display()    
# print("Third Student Details")
# s3.display()
# s3.get_total_student()

class Test(Student):
    def __init__(self,roll,name,address,mobile,sub1,sub2,sub3):
        try:
            if (0<=sub1<=100) and (0<=sub2<=100) and (0<=sub3<=100):
                self.sub1=sub1
                self.sub2=sub2 
                self.sub3=sub3
            else:
                raise InvalideMarks
        except InvalideMarks:
            print("Please enter marks 0 to 100")
        super().__init__(roll,name,address,mobile)        
    
    
    def display_data(self):
        self.display_student()
        print(f"First Subject marks : {self.sub1}")
        print(f"First Subject marks : {self.sub2}")
        print(f"First Subject marks : {self.sub3}")
        
        
s1=Test(101,'shubham','pune','9874563210',78,89,68)
s2=Test(102,'mohan','mumbai','9874563210',78,89,168)
s3=Test(103,'rohan','raipure','9874563210',78,89,-0)
