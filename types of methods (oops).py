

# # instance method

# class student:
    
#     school= "wow university"
    
#     def __init__(self,m1,m2,m3):
#         self.m1=m1
#         self.m2=m2
#         self.m3=m3
    
#     def avg(self):
#         return(self.m1+self.m2+self.m3)/3
    
# s1=student(20,3,25)

# s2=student(20,4,25)

# print(s1.avg())
# print(s2.avg())

# print(s1.m1,s1.m2)

# print(s2.m1,s2.m2)




class student:
    # class variables
    
    school= "wow university"
    
    # constructor
    def __init__(self,m1,m2,m3):
        # instance variables
        self.m1=m1
        self.m2=m2
        self.m3=m3
    
    def avg(self):
        return(self.m1+self.m2+self.m3)/3
    @classmethod
    
    def info(cls,name):
        cls.school_name=name
    
s1=student(20,3,25)

s2=student(20,4,25)

print(s1.avg())
print(s2.avg())

print(student.info)