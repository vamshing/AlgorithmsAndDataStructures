class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 2:
            return 1
        # Use binary search
        l, r = 0, x
        while l <= r:
            m = (l + r) / 2
            if m * m <= x < (m + 1) * (m + 1):
                return m
            else:
                if m * m < x:
                    l = m + 1
                else:
                    r = m - 1
