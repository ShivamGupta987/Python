# n=5
# for i in range(n):        #rows
#     for j in range(5):    #columns
#         print('*',end=" ")
#     print()
    
    
    
    
# # increasing triangle program
# n=5
# for i in range(n):        #rows
#     for j in range(i+1):    #columns
#         print('*',end=" ")
#     print()
    
    
# decreasing triangle program 
# n=5
# for i in range(n):        #rows
#     for j in range(5-i):    #columns
#         print('*',end=" ")
#     print()



# # right sided triangle

# n=5
# for i in range(n):
#     for j in range(i,n):
#         print(' ',end=' ')
        
        
#     for j in range(i+1):
#         print('*',end=' ')
        
#     print()




# # right sided triangle

# n=5
# for i in range(n):
#     for j in range(i+1):
#         print(' ',end=' ')
        
        
#     for j in range(i,n):
#         print('*',end=' ')
        
#     print()




# # hill pattern

# n=5
# for i in range(n):
#     for j in range(i,n):
#         print(' ',end=' ')
        
        
            
#     for j in range(i):
#         print('*',end=' ')
        
        
#     for j in range(i+1):
#         print('*',end=' ')
        
#     print()


# downward hill paterrn

# n=5
# for i in range(n):
#     for j in range(i+1):
#         print(' ',end=' ')
        
        
#     for j in range(i,n-1):
#         print('*',end=' ')
        
#     for j in range(i,n):
#         print('*',end=' ')
        
#     print()


# # diamond pattern

# n=5
# for i in range(n-1):
#     for j in range(i,n):
#         print(' ',end=' ')
        
        
            
#     for j in range(i):
#         print('*',end=' ')
        
        
#     for j in range(i+1):
#         print('*',end=' ')
        
#     print()    
    
#   for i in range(n):
#       for j in range(i+1):
#         print(' ',end=' ')
        
        
    # for j in range(i,n-1):
    #     print('*',end=' ')
        
    # for j in range(i,n):
    #     print('*',end=' ')
        
   
        
    # print()
    
    
    
    
n=5
for i in range(n):
        
    for j in range(i*2-1):
        print('*',end=' ')
        
    print()