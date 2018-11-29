"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.
"""
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Time  : O(N)
        # Space : O(N)
        # Method : Using a hashTable to store the counts of individual elements
        if len(nums) < 2:
            return nums[0]
        else:
            d = dict()
            for item in nums:
                if item in d:
                    d[item] += 1
                else:
                    d[item] = 1
            return [k for (k,v) in d.iteritems() if v == 1][0]

# O(N)
#r = Solution().singleNumber([1,1,2])
#print(r)

# Alternative solution - using XOR gate
l = [4,2,1,2,1]
print(reduce(lambda  x,y : x^y,l)) #O(n) using XOR implementation
