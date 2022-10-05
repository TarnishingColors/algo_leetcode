from collections import Counter


# https://leetcode.com/problems/permutation-in-string/
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1 = len(s1)
        len_s2 = len(s2)

        if len_s1 > len_s2:
            return False

        counter_s1 = Counter(s1)

        i = len_s1
        while i <= len_s2:
            print(s2[i-len_s1:i])
            print(Counter(s2[i-len_s1:i]), counter_s1)
            print(Counter(s2[i-len_s1:i]) == counter_s1)
            if Counter(s2[i-len_s1:i]) == counter_s1:
                return True
            i += 1
        return False
