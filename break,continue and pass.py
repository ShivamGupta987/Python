# Python program to

# loop from 1 to 10
for i in range(1, 11):
	
	# If i is equals to 6,
	# continue to next iteration
	# without printing
	if i == 6:
		continue
	else:
		# otherwise print the value
		# of i
		print(i, end = " ")
  
  
  
  
  # Python program to demonstrate
# pass statement


s = "geeks"

# Empty loop
for i in s:
	# No error will be raised
	pass

# Empty function
def fun():
	pass

# No error will be raised
fun()

# Pass statement
for i in s:
	if i == 'k':
		print('Pass executed')
		pass
	print(i)



