data={1:'navin',2:'shivam',4:'parvez'}
print(data)
print(data[4])
print(data[2])
print(data.get(1,'notfound'))
print(data.get(3,'notfound'))
# now we uses key
keys=['sultan','parvez','shivam']
values=['hindi','science','maths']
# for dictionary we uses zip for Eexample (sultan like science) 
data=dict(zip(keys,values))
print(data)
print(data['shivam'])
print(data['parvez'])
# for adding new 
data['shiv']='cs'
print(data)
del data['shivam']
print(data)
# we create a new dictionary list inside a dictionary
# uses prog {}
prog ={'js':'atom','cs':'vs','python':['pycharm','sublime'],'java':{'JSE':'NETBEANS','JEE':'ECLIPSE'}}
print(prog)
# advantage is we can simply find anything 
print(prog['js'])
print(prog['python'])
print(prog['java']['JEE'])