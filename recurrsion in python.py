# max deptth recurssion 1000 times only


# def greet(): 
    
#     print("hello")
    
#     greet()
# greet()  # recurssionlimit

# now we set limit own

# import sys

# sys.setrecurrsionlimit(500)
# print('sys.getrecurrsionlimit()')
# i=0
# def greet ():
    
#     global i    #not running in rucurssion attribute error  
#     i+=1
#     print("hello", i)
#     greet()
# greet()  




#####    RECURRSION IN FACTORIAALLLL

def fact (n):
    
    if n==0:
        
        return 1
    
    return n*fact(n-1)

result =  fact(5)

print(result)



def fact (n):
    
    if n==0:
        
        return 1
    
    return n*fact(n-1)

result =  fact(6)

print(result)