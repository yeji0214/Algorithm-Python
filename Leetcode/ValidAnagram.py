class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_res = {}
        t_res = {}

        for S in s:
            s_res[S] = s_res.get(S, 0) + 1

        for T in t:
            t_res[T] = t_res.get(T, 0) + 1

        if s_res == t_res:
            return True
        return False