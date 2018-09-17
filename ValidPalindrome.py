"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.
"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Time : O(N)
        # Space : O(N)
        # method : reverse the string and compare
        if(s==""):
            return True
        s = s.lower().strip()
        s = ''.join(char for char in s if char.isalnum())
        return(s == s[::-1])


s = ""
print(Solution().isPalindrome(s))
