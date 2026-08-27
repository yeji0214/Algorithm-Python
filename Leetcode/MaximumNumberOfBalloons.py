class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        ans = 0
        cnt = {}
        word = 'balloon'

        for t in text:
            cnt[t] = cnt.get(t, 0) + 1

        while True:
            for w in word:
                if w not in cnt or cnt[w] == 0:
                    return ans
                cnt[w] -= 1
            ans += 1

        return ans