"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice

Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1]
"""


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Space complexity : O(N)
        # Time  complexity : O(N)
        # Data Structure used : HashTable / pythonDictionary
        if(len(nums) > 1):
            d = {}
            for i in range(len(nums)):
                if nums[i] in d.values():
                    return [list(d.values()).index(nums[i]), i]
                else:
                    d[i] = target - nums[i]


# l = [2,7,11,15]
# c = Solution().twoSum(l, 9)
# print(c)
# [0,1]
