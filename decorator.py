# use this function without modifying itself  

def div(a,b):
    
    print(a/b)
    
def smart_div(func):
    
# functiion into function is only python...
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    
    return inner

div=smart_div(div)
div(2,4)

div(6,8)




# subtraction

def sub(a,b):
    
    print(a-b)
    
def smart_sub(func):
    
# functiion into function is only python...
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    
    return inner

sub=smart_sub(sub)
sub(2,4)


