

# add 2 numbers
print(100 + 200)

# concatenate two strings
print('Jess' + 'Roy')

# merger two list
print([10, 20, 30] + ['jessa', 'emma', 'kelly'])




class Book:
    def __init__(self, pages):
        self.pages = pages

    # Overloading + operator with magic method
    def __add__(self, other):
        return self.pages + other.pages

b1 = Book(400)
b2 = Book(300)
print("Total number of pages: ", b1 + b2)





class Employee:
    
    def __init__(self, name, salary):
        
        self.name = name
        self.salary = salary

    def __mul__(self, timesheet):
        
        print('Worked for', timesheet.days, 'days')
        
        # calculate salary
        
        return self.salary * timesheet.days


class TimeSheet:
    def __init__(self, name, days):
        
        self.name = name
        self.days = days


emp = Employee("Jessa", 800)

timesheet = TimeSheet("Jessa", 50)

print("salary is: ", emp * timesheet)
