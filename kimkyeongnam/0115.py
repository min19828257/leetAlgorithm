class Solution:
    def getMaximumGenerated(self, n: int) -> int:
    
    # Solution 1
        if n == 0 or n == 1:
            return n
        nums = [0] * (n + 1)
        nums[1] = 1
        for i in range(2, n + 1):
            nums[i] = nums[i // 2] if i % 2 == 0 else nums[i // 2] + nums[i // 2  + 1]
        return max(nums)

    # Solution 2        
        if n == 0 or n == 1:
            return n
        nums = [0] * (n + 1)
        nums[1] = 1        
        cur_max = 1
        for i in range(1, n + 1):
            if 2 <= 2 * i <= n:
                nums[2 * i] = nums[i]
            if 2 <= 2 * i + 1 <= n:
                nums[2 * i + 1] = nums[i] + nums[i + 1]
            cur_max = max(cur_max, nums[i])
        return cur_max
    
