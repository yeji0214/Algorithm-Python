class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        money = {5: 1, 10: 0}

        if bills[0] != 5:
            return False

        for i in range(1, len(bills)):
            if bills[i] == 5:
                money[5] += 1
            elif bills[i] == 10:
                money[10] += 1
                if money[5] > 0:
                    money[5] -= 1
                else:
                    return False
            else:
                if money[5] > 0 and money[10] > 0:
                    money[5] -= 1
                    money[10] -= 1
                elif money[5] >= 3:
                    money[5] -= 3
                else:
                    return False
        return True