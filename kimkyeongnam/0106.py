"""Kth Missing Positive Number"""


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # ex1: arr = [2,3,4,7,11], k = 5,  ans: 9
        # ex2: arr = [1,2,3,4], k = 2,     ans: 6
        
        origin = set(i for i in range(1, arr[-1] + 1 + k))
        diff = list(origin - set(arr))
        diff.sort()
        return diff[k - 1]
