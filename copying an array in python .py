# from numpy import *
# arr =array([1,2,3,4,5])


# arr1 = arr+5

# print(arr1)

# from numpy import *

# arr1 =array([1,2,3,4,5])
# arr2 =array([9,8,7,6,5])
# arr3 =arr1 + arr2
# print(arr3)

# new


# from numpy import *

# arr1 =array([1,2,3,4,5])

# arr2 =array([9,8,7,6,5])
# print([concatenate([arr1,arr2])])


# from numpy import *

# arr1 =array([1,2,3,4,5])
# print(min(arr1))
# print(max(arr1))
# print(sqrt(arr1))
# print(sin(arr1))
# print(log(arr1))
# print(cos(arr1))
# print(tan(arr1))
# print(arr1*arr1)

# copying an array

# from numpy import *

# arr6 = array([4,6,5,9])
# arr5=arr6
# print(arr5)
# print(arr6)
# print(id(arr5))
# print(id(arr6))


#  two types of copy shallow and deep copy
# in shallow uses view()
# in deep uses copy()

# from numpy import *

# arr6 = array([4,6,5,9])
# arr5=arr6
# arr6[2]=3
# print(arr5)
# print(arr6)
# print(id(arr5))
# print(id(arr6))




# from numpy import *

# arr6 = array([4,6,5,9])
# arr5=arr6.view() #known as shallow 
# arr6[2]=3
# print(arr5)
# print(arr6)
# print(id(arr5))
# print(id(arr6))



from numpy import *

arr6 = array([4,6,5,9])
arr5=arr6.copy() #known as deep copy means different  
arr6[2]=3
print(arr5)
print(arr6)
print(id(arr5))
print(id(arr6))










