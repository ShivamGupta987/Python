nums=[24,26,76,89,22]
print(nums)
names=['shivam','aditya','sunil']
print(names)
# append means add value insert always in betwween add but append last 
nums.append(45)
print(nums)
nums.insert(30,23)
print(nums)
nums.pop(2)
print(nums)
# remove multiple value then uses (del) for add uses (extend)
del nums[2:4]
print(nums)
nums.extend([12,13])
print(nums)
print(min(nums))
print(max(nums))
nums.sort()
print(nums)