class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        ans = []
        idx_sum = 2000

        for i in range(len(list1)):
            s = list1[i]
            if s in list2:
                result = i + list2.index(s)
                if idx_sum > result:
                    ans = []
                    idx_sum = result
                    ans.append(s)
                elif idx_sum == result:
                    ans.append(s)

        return ans