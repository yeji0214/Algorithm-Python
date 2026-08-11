class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num = num[::-1]
        k = list(str(k))[::-1]
        result = []

        i = 0
        nxt = 0
        while k or num:
            if not k:
                a = num.pop(0)
                result.append((a + nxt) % 10)
                nxt = (a + nxt) // 10
            elif not num:
                b = int(k.pop(0))
                result.append((b + nxt) % 10)
                nxt = (b + nxt) // 10
            else:
                a, b = num.pop(0), int(k.pop(0))
                print(a, b)
                result.append((a + b + nxt) % 10)
                nxt = (a + b + nxt) // 10
        if nxt > 0:
            result.append(nxt)

        return result[::-1]