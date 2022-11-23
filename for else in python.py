# # in python we use if else now we use for else intrestinggggg
# nums=[10,12,35,47,98]
# for num in nums:
#     if num %5==0:
#         print(num)
        
# # but we won't any one number divisble by 5 now we use (break)
# nums=[10,12,35,47,98]
# for num in nums:
#     if num %5==0:
#         print(num)
#         break
     
# nums=[16,12,39,47,98]
# for num in nums:
#     if num %5==0:
#         print(num)
#         break

# else:
#     print("not found")

# #  if we dont use break then (not found ) always  print e.g.
# nums=[15,12,39,47,98]
# for num in nums:
#     if num %5==0:
#         print(num)

# else:
#     print("not found")
# # that,s why we use break ....

# check prime or not????

num=7
for i in range(2,num):
    if num %i==0:
        print('not prime')
        break  #uses because we can clarify
else:
    print("prime")