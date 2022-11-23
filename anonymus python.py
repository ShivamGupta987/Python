
def square(a):
    return a*a

result= square(5)
print(result)


# now we use anonymus function (lambda)

f= lambda a:a*a
result=f(5)
print(result)



f= lambda a,b:a*b
result=f(5,6)
print(result)



f= lambda c,d:c+d
result=f(5,6)
print(result)