class Solution:
    def countVowelStrings(self, n: int) -> int:
        if n == 0:
            return 0
        
        counts = [1] * 5
        while n > 1:
            # 1 1 1  1  1  -> 5
            # 1 2 3  4  5  -> 15
            # 1 3 6  10 15 -> 35
            # 1 4 10 20 35 -> 70
            for i in range(1, 5):
                counts[i] += counts[i - 1]
            n -= 1

        return sum(counts)
