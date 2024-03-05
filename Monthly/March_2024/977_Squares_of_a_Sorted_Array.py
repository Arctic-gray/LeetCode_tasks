'''
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
'''
nums = [-7, -3, 2, 3, 11]

square_nums = list(map(lambda x: x ** 2, nums))

print(sorted(square_nums))
