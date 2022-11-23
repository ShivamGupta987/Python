# def update (x):
#     print(id(x))
    
#     x=8
#     print(id(x))
#     print("x",x)

# a=10
# print(id(a))
# update(a)
# print("a",a)



# def update (lst):
#     print(id(lst))
#     lst[1]=25
    
#     print(id(lst))
#     print("x",lst)

# lst=[10,20,30]
# print(id(lst))
# update(lst)
# # print("lst",lst)   id should be same therefore number should also be equal



# types of argumentsss

# def person(name,age):
#     print(name)
#     print(age)
    
# person('navin',28)  #if we change the (1st type)position there should be error


# if we change the positoon then we use (2nd type of argument)="keyword" example

# def person(name,age):
#     print(name)
#     print(age)

# person(age=18,name='shivam')


# 3rd type "default" uses when if one is not given but we agreed one value define


# def person(name,age=17):
#     print(name)
#     print(age)

# person('shivam')




# 4th type "variable length"


#(*b)meaning if more than one value of b is given then they yake any one value at a time

# def multiplier(*num):
#     prod=1
# #initialize prod variable with zero    
#     for i in num:
#         prod = prod * i

#     print("Product:",prod)

# multiplier(3,5)
# multiplier(1,2,4)
# multiplier(2,2,6,7)




# def person (name,*data):
#     print(name)
#     print(data)
    
# person('shivam',18,"goregaon",987657865)


# for mltilpe data we uses(**data) keyword variable lenth arguments

# def person(name,**data):
#     print(name)
#     print(data)

# person("shivam",age=18,state="goregaon",mob=9987648763)

# # we also uses for loop 
# def person(name,**data):
#     print(name)
#     for i,j in data.items():
#         print(i,j)
        
        
# person("bheem",age=15,state="dholakpur",mob=9987648763)
