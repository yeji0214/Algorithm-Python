class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        info = []

        for i in range(len(names)):
            info.append([names[i], heights[i]])

        info = sorted(info, key=lambda x:-x[1])
        res = []

        for i in range(len(info)):
            res.append(info[i][0])

        return res