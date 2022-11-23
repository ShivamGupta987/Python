# four method for swapping
# 1st method
a=5
b=6
temp=a
a=b
b=temp
print(a)
print(b)
# using swap without using (third variable)
a=5
b=6
a=a+b #11
b=a-b #5
a=a-b #6
print(a)
print(b)
# 3rd method using (xor)
a=5
b=6
a=a^b
b=a^b
a=a^b
print(a)
print(b)
# 4th method
# this is performed by solve firsst right hand side....
a=5
b=6
a,b=b,a
print(a)
print(b)