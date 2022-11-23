x=9
r=x%2
if r==0:
    print('even')
if r==1:
    print('odd')    

#  as a prograamer we can work efficient ways then we uses (else) if we uses 2 if then check both all time then we use else vriable
#  we see if else we uses colon(:)

x=8
r=x%2
if r==0:
    print('even')
else:
    print('odd')    
    
x=73
r=x%2
if r==0:
    print('even')
else:
    print('odd')   
    
# now we use two if known as (nested if)
x=12
r=x%2
if r==0:
    print('even')
    if r>5:
        print("shivam")
    else:
        print('not shivam')   
else:
    print('odd')    
    
# elif used we cn check only once not all statement :-if it is true then 'ok' otherwise check not at all
x=5
if x==1:
    print('one')
elif x==2:
    print('two')
elif x==3:
    print('three')
elif x==4:
    print("four")
else :
    print('wrong input')                