nums = [1, 2, 3, 4]
 
#Sort the list from smallest to largest.
nums.sort()
 
#Find the median.
length = len(nums)
if (length % 2 == 0):
    median = (nums[(length)//2] + nums[(length)//2-1]) / 2
else:
    median = nums[(length-1)//2]
 
#Display the result.
print(median)
