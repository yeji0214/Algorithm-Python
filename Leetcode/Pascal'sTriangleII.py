class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle = [[] for _ in range(34)]
        triangle[0] = [1]
        triangle[1] = [1, 1]

        if rowIndex <= 1:
            return triangle[rowIndex]
        
        for i in range(2, rowIndex + 1):
            triangle[i].append(1)
            for j in range(i - 1):
                triangle[i].append(triangle[i - 1][j] + triangle[i - 1][j + 1])
            triangle[i].append(1)

        return triangle[rowIndex]