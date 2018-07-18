class Solution(object):
    def findLengthOfLCIS_DP(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Using Dynamic programming time -> O(N) space -> O(N)
        if not nums:
            return 0
        d = [1 for i in range(len(nums))]
        print d
        for i in range(1, len(nums)):
            print i
            if nums[i] > nums[i - 1]:
                d[i] = max(d[i - 1], d[i - 1] + 1)
        print d
        return max(d)

    def findLengthOfLCIS(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # Without using Space
    # Time -> O(N)
    if not nums:
        return 0
    # c - current length of increasing subseq
    # m - max of the length of longest increasing subsequence
    c, m = 1, 1
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            c += 1
            m = max(m, c)
        else:
            c = 1
    return m
