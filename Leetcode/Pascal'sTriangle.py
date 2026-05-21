class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]

        res = [[1], [1, 1]]

        for i in range(numRows - 2):
            lst = res[-1]
            arr = []
            for j in range(len(lst) - 1):
                arr.append(lst[j] + lst[j + 1])
            res.append([1] + arr + [1])

        return res