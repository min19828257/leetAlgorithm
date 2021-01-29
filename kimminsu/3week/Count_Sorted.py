class Solution(object):
    
    def countVowelStrings(self, n):
        """
        :type n: int
        :rtype: int
        """
        sentence = ['a','i','o','u','e']
        self.sorted_vowels = sorted(sentence)
        self.number = 0

        def recursive(current_index, last_index, cnt, goal_cnt):
            cnt += 1
            if cnt == goal_cnt:
                self.number += 1
                return

            for i in range(current_index, last_index):
                  recursive(i, last_index, cnt, goal_cnt)

        for index in range(len(self.sorted_vowels)):
            recursive(index, len(self.sorted_vowels), 0, n)

        return self.number