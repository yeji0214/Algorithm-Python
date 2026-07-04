class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ans = ''
        step = 2 * k

        idx = 0
        while idx < len(s):
            if idx + step >= len(s):
                current = s[idx:]
                idx = len(s)
            else:
                current = s[idx:idx + step]
                idx += step

            if len(current) < k:
                ans += current[::-1]
            else:
                ans += current[:k][::-1]
                ans += current[k:]
        
        return ans