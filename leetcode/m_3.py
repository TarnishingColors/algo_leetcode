# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = j = 0
        max_len = 0
        while i < len(s):
            if len(set(s[i:j])) == len(s[i:j]):
                max_len = max(j - i, max_len)
                if j >= len(s):
                    break
                j += 1
            else:
                i += 1
        return max_len
