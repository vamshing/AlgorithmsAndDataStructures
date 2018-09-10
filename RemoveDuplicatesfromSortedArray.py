class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Time O(n)
        # Space inplace
        # Method : while loop to manipulate a list in place
        n = 1
        while n < len(nums):
            if(nums[n] == nums[n - 1]):
                nums.pop(n)
            else:
                n += 1
        return len(nums)


obj = Solution().removeDuplicates([2, 2, 2, 3, 4])
print(obj)
