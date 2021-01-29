import copy
class sol:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target
        self.current_state = 0

        self.count = 0

    def front_run(self):
        self.end_recursive()
        return self.count

    def end_run(self):
        self.front_recursive()
        return self.count
        
    def front_recursive(self):
        data = self.nums[0]
        print("extracted data : ", data, self.nums)

        test = self.current_state + data
        if test > self.target :
            print("front excess : ", self.current_state, self.nums)
            return -1
        elif test == self.target:
            self.current_state += self.nums.pop(0)
            self.count += 1
            print("collision : ", self.current_state, self.nums)
            return 0
        else:
            self.current_state += self.nums.pop(0)
            self.count += 1
            self.front_recursive()
            self.end_recursive()

    def end_recursive(self):
        data = self.nums[-1]
        print("extracted data : ", data, self.nums)

        test = self.current_state + data
        if test > self.target :
            print("excess : ", self.current_state, self.nums)
            return -1
        elif test == self.target:
            self.current_state += self.nums.pop(-1)
            self.count += 1
            print("collision : ", self.current_state, self.nums)
            return 0
        else:
            self.current_state += self.nums.pop(-1)
            self.count += 1
            self.end_recursive()
            self.front_recursive()

class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        sto = copy.deepcopy(nums)
        
        s = sol(nums, x)
        front_result = s.front_run()
        print("front result : ", front_result)
        print("----------------")
        e = sol(sto, x)
        end_result = e.end_run()
        
        print("end result : ", end_result)
        
        if front_result > end_result:
            mini = end_result
        elif front_result < end_result:
            mini = front_result
        else:
            mini = front_result
        
        if mini == 0:
            return -1
        return mini