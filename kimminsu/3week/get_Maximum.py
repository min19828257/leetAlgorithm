import sys
sys.getrecursionlimit()

class Solution(object):
    def discr(self, num, cnt):
        if num == 1:
            return 1
        elif num == 0:
            return 0

        if num%2 == 1:
            cnt += self.discr(int(num/2),cnt) + self.discr(int(num/2)+1,cnt)
        else:
            cnt += self.discr(num/2, cnt)

        return cnt
    
    def getMaximumGenerated(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n%2 == 0:
            result = self.discr(n-1, 0)
        else:
            result = self.discr(n, 0)
        
        return result