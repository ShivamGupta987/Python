
# 1st type object and class (in this case we define function itself )

# class computer:
#     def config(self):
#         print("i5,16gb,1TB")



# a="8"
# print(type(a))
# com1=computer()
# print(type(com1))




class computer:
    
    def config(self):
        print("i5,16gb,1TB")

com1=computer()
computer.config(com1)


# for double print same we use com2
class computer:
    
    def config(self):
        print("i5,16gb,1TB")

com1=computer()

com2=computer()

computer.config(com1)    # in place of computer.config we usee com1.config()    
computer.config(com2)    # in place of computer.config we usee com2.config()    


#in this case we use object itself to call a function

com1.config()

com2.config()


