"""
Count the number of prime numbers less than a non-negative number, n.
Input: 10 ;Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
"""

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Time Complexity  : O(n log n )
        # Space Complexity : O(n)
        # Algorithm used : Sieve of Eratosthenes
        # https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
        if n > 2:
            l = [True] * n
            for i in range(l):
                if(l[i]):
                    for i in range(n + 1, i)[1:]:
                        [i] = False
            return sum(l)
        else:
            return 0


numPrimes = Solution().countPrimes(11)
print(numPrimes)
