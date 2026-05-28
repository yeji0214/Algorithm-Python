class NumArray:
    n = []

    def __init__(self, nums: List[int]):
        self.n = nums

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.n[left:right+1])