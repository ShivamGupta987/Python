x=2
y=3
print(x+y)
print(x-y)
print(x*y)
print(x/y)
#we uses assignment operator
x=x+2
print(x)
# for easy way we do
x+=2
print(x)
x*=2
print(x)
# assignment in one line
a,b=5,6
print(a)
print(b)
# for unary operators
n = 7
print(n)
print(-n)
n=-n
print(n)
# relation operators
a=5
b=6
x=a<b
print(x)
x=a>b
print(x)
# double equal is comparing not assgning  
x=a==b
print(x)
a=6
b=6
x=a==b
print(x)
# now we use less than or greather than equal to x<=,x>=
x=a<=b
print(x)
x=a>=b
print(x)
# for not we use (!)this sign
# logical operator (and,or,not)
x=a!=b
print(x)
a=5
b=4
x=a<8 and b<5
print(x)
x=a<8 and b<2
print(x)
x=a<8 or b<2
print(x)
# BITWISE OPERATORS
# complement operator(~)
x=~12
print(x)
x=~5
print(x)
# we cant store negative number(-ve)system always(+ve) number store
#   bitwise (and) operator
x=12&13
print(x)
x=5&6
print(x)
x=7&8
print(x)
# BITWISE OR(|) OPERATOR
x=5|4
print(x)
x=32|34
print(x)
x=9|10
print(x)
x=25|30
print(x)
# BITWISE XOR(^) OPERATOR
x=12^13
print(x)
x=25^30
print(x)
# LEFT SHIFT(<<) OPERATOR
x=10<<2   #2 denote as shift
print(x)
x=25<<24
print(x)
x=11<<8
print(x)