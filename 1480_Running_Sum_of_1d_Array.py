'''
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.
'''
nums = [3, 1, 2, 10, 1]

numsSum = []
sum = 0

for i in range(len(nums)):
  sum += nums[i]
  numsSum.append(sum)

print(numsSum)
