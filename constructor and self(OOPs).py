
# class computer:
#     pass

# c1=computer()    #c1 and c2 are constructor
# c2=computer()

# print(id(c1))
# print(id(c2))


# class computer:
#     def _init_(self):
#         self.name='shivam'   # self I used for assigned the object
#         self.age=18          # either me or you ----does self work
        
# c1=computer()
# c2=computer()

# c1.name='vishnu'
# c1.age=16

# print(c1.name)

# print(c1.age)


class computer:
     def __init__(self, name, age):
        self.name=name
        self.age=age
    
     def show(self):
         print('Name:', self.name, self.age)
        
c1=computer("shivam", 10)
print(c1.show())

# c1.name='vishnu'
# c1.age=16

# c1.update()

# print(c1.name)
# print(c1.age)
      

      
