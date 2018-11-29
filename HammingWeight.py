"""
Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).
Input: 11
Output: 3
Explanation: Integer 11 has binary representation 00000000000000000000000000001011
"""
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return "{0:b}".format(n).count('1')

print(Solution().hammingWeight(11))
