class Solution:
    def thousandSeparator(self, n: int) -> str:
        ans = []
        n = str(n)[::-1]
        current = 0

        for N in n:
            current += 1
            ans.append(N)
            if current % 3 == 0 and current < len(n):
                ans.append('.')
        
        return ''.join(ans)[::-1]