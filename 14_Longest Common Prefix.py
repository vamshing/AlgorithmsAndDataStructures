"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # Run time Complexity : O(N^2)
        # Space Complexity    : O(N)
        # Method :

        def gen_prefix(a, b):
            # Returns the largest prefix amongst two strings
            # Optimize by picking the prefix to be the one with the minimum length
            prefix = a
            while(prefix != ""):
                if b.startswith(prefix):
                    return prefix
                    break
                else:
                    prefix = prefix[:-1]

            return prefix

        commonprefixes = []

        if len(strs) < 1:
            return ""

        if len(strs) == 1:
            return strs[0]

        for i in range(0, len(strs)):
            for j in range(i + 1, len(strs)):
                prefix = gen_prefix(strs[i], strs[j])
                if prefix == '':
                    return ""
                else:
                    commonprefixes.append(prefix)

        return min(commonprefixes)
