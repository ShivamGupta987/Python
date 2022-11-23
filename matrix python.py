# multidimensional array in python 


# now uses matrix

# from numpy import*
# m=matrix('1 2 3; 4 5 6;7 8 9')
# print(m)

# if i nee 2 rows and 2 column just put semicolon after 2 value
# from numpy import*
# m=matrix('1 2; 3 4 ;5 6 ;7 8 ')
# print(m)
# print (diagonal(m)) # we want only diagonal element
# print(m.min())
# print(m.max())



# multipy of 2 matrix

from numpy import *
m1= matrix('1 2 3 ;4 5 6 ;7 8 9 ')
m2= matrix('4 3 5 ; 7 6 5 ; 1 3 8 ')
m3=m1*m2 ;
print(m3)