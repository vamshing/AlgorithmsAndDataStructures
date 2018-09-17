# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Space O(N)
        # Time O(N)
        # Method - use a dict to look up the frequency of the first non-repeating character
        # Required - collections.Counter
        from collections import Counter
        d = Counter(s)
        for i, character in enumerate(s):
            if d[character] == 1:
                return i
        return -1


print(Solution().firstUniqChar('loveleetcode'))
