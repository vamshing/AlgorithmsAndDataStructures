class Solution(object):
    def lengthOfLIS_DP(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Dyanmic programming
        # initialize the array D
        # time -> O(N^2) space -> O(N)
        if not nums:
            return 0
        D = [1 for i in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    D[i] = max(D[i], D[j] + 1)
        print D
        return max(D)
