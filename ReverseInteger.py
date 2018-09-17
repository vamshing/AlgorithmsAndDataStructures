class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x_ = int(str(abs(x))[::-1]) * cmp(x,0)
        if x_ < -2**31 or x_ > 2**31 - 1:
            return 0
        else:
            return x_


print(Solution().reverse(-12399999000))
