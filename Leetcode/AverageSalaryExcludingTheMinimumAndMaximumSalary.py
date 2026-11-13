class Solution:
    def average(self, salary: list[int]) -> float:
        salary.sort()
        salary = salary[1:-1]

        return sum(salary) / len(salary)