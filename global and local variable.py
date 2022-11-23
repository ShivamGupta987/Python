a=10
def something():
    a=15  #local variable  is two line and all are global 
    print(a)
    
print(a) 



# if we want only 10 then we use global
# a=10
# def something():
#     global a
#     a=15  
#     print("inside",a)
    
# print("outside",a)


# we uses 3 or 4 value then uses globals
# a=10
# print(id(a))
# def something():
#     a=15  
#     x=globals()["a"]
#     print(id(x))
#     print("inside",a)
    
# something()

# if we change global without affecting local just type
a=10
print(id(a))

def something():
    a=9
    x=globals()["a"]
    
    print(id(x))
    
    print("inside",a)
    
    globals()["a"]=20
    
something()