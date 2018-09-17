"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string ""
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        c = 999999999
        shortest = reduce(lambda x, y: x if (len(x) < len(y)) else y, strs)
        strs.remove(shortest)
        for word in strs:
            shortest_ = shortest
            while(shortest_ != ""):
                if(word.find(shortest_)) != 0:
                # shave the shortest_
                    shortest_ = shortest_[:-1]
                else:
                    c =
                    break
        if c == 999999999:
            return ""
        else:
            return shortest[:c]


l = ["fl", "flowet", "flight"]
print(Solution().longestCommonPrefix(l))
