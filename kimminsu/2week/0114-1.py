import bisect
class Solution(object):
    def createSortedArray(self, instructions):
        """
        :type instructions: List[int]
        :rtype: int
        """
        answer = 0
        arr = []
        n = len(instructions)
        MOD = 10 ** 9 + 7
        for i, inst in enumerate(instructions):
            l = bisect.bisect_left(arr, inst)
            r = bisect.bisect(arr, inst)
            answer += min(l, i - r)
            arr[r:r] = [inst]
        return answer % MOD
