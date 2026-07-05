class Solution:
    def checkRecord(self, s: str) -> bool:
        if s.count('A') >= 2:
            return False

        late = 0
        for S in s:
            if S == 'L':
                late += 1
                if late >= 3:
                    return False
            else:
                late = 0

        return True