class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        invert = {0: 1, 1: 0}
        result = []

        for i in image:
            result.append(i[::-1])

        n = len(image)
        for i in range(n):
            for j in range(n):
                result[i][j] = invert[result[i][j]]

        return result