# this method is very customised so we use this method

# nums = [2,3,4,5,6,7]

# evens = list(filter(lambda n :n%2==0,nums))
# print(evens)    
# THIS IS THE BEAUTY OF LAMBDA


# nums = [2,3,4,5,6,7]

# evens = list(filter(lambda n :n%2==0,nums))

# doubles =list(map(lambda n:n*2,evens))
# print(doubles) 

# in reduce we use (function,sequence) we import functool use

from functools import reduce

nums = [2,3,4,5,6,7]

evens = list(filter(lambda n :n%2==0,nums))

doubles =list(map(lambda n:n*2,evens))

print(doubles) 

sum = reduce(lambda a,b : a+b,doubles)

print(sum)