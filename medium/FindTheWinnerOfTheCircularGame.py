class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        numbersList = list(i for i in range(n))
        curIdx = 0
        for x in range(n-1):
            curIdx = (curIdx + k - 1 ) % (len(numbersList))
            del numbersList[curIdx]
        return numbersList[0] + 1


solution = Solution()
print(solution.findTheWinner(6, 5))