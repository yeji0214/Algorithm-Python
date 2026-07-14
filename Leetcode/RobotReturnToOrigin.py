class Solution:
    def judgeCircle(self, moves: str) -> bool:
        move = {'R': [1, 0], 'L': [-1, 0], 'U': [0, 1], 'D': [0, -1]}
        x, y = 0, 0

        for m in moves:
            x += move[m][0]
            y += move[m][1]

        if x == 0 and y == 0:
            return True
        return False