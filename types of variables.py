

# class car:
    
    
#     def __init__(self, mil, com):
        
        
#         self.mil=mil      #instance variable
#         self.com=com      ]][#instance variable
        
        
        
# c1=car("10","BMW")

# c2=car(20,"lMBORGINI")

# print(c1.com, c1.mil)

# print(c2.com,c2.mil)





class car:
    
    
    def __init__(self, mil, com,wheels):
        
        
        self.mil=mil        #instance variable
        self.com=com        #instance variable
        self.wheels=wheels  
        
        
        
c1=car("10","BMW",4)

c2=car(20,"lMBORGINI",4)

print(c1.com, c1.mil,c1.wheels)

print(c2.com,c2.mil,c2.wheels)
