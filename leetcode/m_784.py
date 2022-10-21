from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        len_s = len(s)
        result = []

        def permutation(pos, st):
            if pos == len_s:
                if st not in result:
                    result.append(st)
            else:
                if type(s[pos]) is str:
                    permutation(pos + 1, st[:pos] + st[pos].lower() + st[pos+1:])
                    permutation(pos + 1, st[:pos] + st[pos].upper() + st[pos+1:])
                else:
                    permutation(pos + 1, st)

        permutation(0, s)

        return result
