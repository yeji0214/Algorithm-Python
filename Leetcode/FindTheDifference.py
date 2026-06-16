class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if not s:
            return t

        result_s = {}
        result_t = {}

        for S in s:
            result_s[S] = result_s.get(S, 0) + 1

        for T in t:
            result_t[T] = result_t.get(T, 0) + 1

        for r in result_t:
            if r not in result_s or result_s[r] != result_t[r]:
                return r