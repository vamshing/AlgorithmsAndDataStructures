class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Time complexity O(N)
        # Space complexity O(N)
        if not nums:
            return 0
        D = nums
        for i in range(1, len(nums)):
            D[i] = max(nums[i] + nums[i - 1], D[i])
        return max(D)
