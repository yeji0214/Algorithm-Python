class Solution:
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key=lambda x:-x[1])
        ans = 0

        for box in boxTypes:
            b1, b2 = box[0], box[1]

            if b1 <= truckSize:
                ans += (b1 * b2)
                truckSize -= b1
            else:
                ans += (truckSize * b2)
                truckSize = 0

            if truckSize == 0:
                return ans
        return ans