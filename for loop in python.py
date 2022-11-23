# i represent 1 list at a time.for loop give value one by one
x=['shivam',23,2.3]
for i in x:
    print(i)
    
x='shivam'
for i in x:
    print(i)
    
x=range(10)
for i in x:
    print(i)
    
# same as both output is same
for i in range(10):
    print(i)
    
# 1 (3rd number represent difference)
for i in range(11,21,1):
    print(i)

for i in range(11,21,5):
    print(i)
    
# we also print reverse (-1)
for i in range(20,11,-1):
    print(i)

#  for in (if statement uses)

for i in range (1,21):
    if i%5!=0:
        print(i)
        
for i in range (1,21):
    if i%5==0:
        print(i)  