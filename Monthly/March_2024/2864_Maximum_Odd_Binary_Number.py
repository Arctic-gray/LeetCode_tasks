'''
You are given a binary string s that contains at least one '1'.
You have to rearrange the bits in such a way that the resulting binary number is the maximum odd binary number that can be created from this combination.
Return a string representing the maximum odd binary number that can be created from the given combination.
Note that the resulting string can have leading zeros.
'''
s = '0101'
out = sorted(list(s), reverse=True)

print(''.join(out[1:]) + '1')
