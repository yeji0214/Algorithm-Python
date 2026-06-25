class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        splitedKey = s.upper().split('-')
        str_key = ''.join(splitedKey)
        ans = []

        first_size = len(str_key) % k

        if first_size > 0:
            ans.append(str_key[0:first_size])
        
        for i in range(first_size, len(str_key), k):
            ans.append(str_key[i:i + k])

        return '-'.join(ans)