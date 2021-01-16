"""
Longest Substring Without Repeating Characters
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        """
        Input: s = "pwwkew"
        Output: 3

        Input: s = "abcabcbb"
        Output: 3

        Input: s = "bbbbb"
        Output: 1
        """
        size = len(s)
        if size < 2 :
            return size
        
        current_longest = 0
        sub = ""

        for c in s:
            if c not in sub:
                sub += c
                if len(sub) > current_longest:
                    current_longest = len(sub)
            else:
                sub = f'{sub.split(c)[1]}{c}'  # "abcabcbb", "abca"->"bca"
        return current_longest
